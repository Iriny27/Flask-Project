import pytest
from flask import Flask, session
from app import app, get_db_connection


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Initialize the test database
    with app.app_context():
        conn = get_db_connection()
        with app.open_resource('test_schema.sql', mode='r') as f:
            conn.executescript(f.read())
        conn.close()

    yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Registration Form" in response.data


def test_register(client):
    data = {
        'full_name': 'John Doe',
        'email': 'john@example.com',
        'phone_number': '1234567890',
        'birth_date': '1990-01-01',
        'gender': 'Male',
        'address_line1': '123 Main St',
        'address_line2': '',
        'country': 'USA',
        'city': 'New York',
        'region': 'NY',
        'postal_code': '12345'
    }

    response = client.post('/register', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration Successful" in response.data

    # Check if the data is inserted into the test database
    with app.app_context():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM registrations WHERE full_name = 'John Doe'")
        row = cur.fetchone()
        assert row is not None
        assert row['email'] == 'john@example.com'
        assert row['phone_number'] == '1234567890'
        # Add more assertions for other fields
        conn.close()


if __name__ == '__main__':
    pytest.main()