import requests
import pytest

BASE_URL = 'http://127.0.0.1:5000/'

@pytest.fixture
def clear_database():
    # Optional: Clear the database before running each test
    # Example: Perform database cleanup if needed
    pass

def test_submit_form():
    # Test submitting the form data
    registration_data = {
        'full_name': 'John',
        'email': 'john@example.com',
        'phone_number': '1234567890',
        'birth_date': '01-01-1990',
        'gender': 'male',
        'address_line1': '123 Main St',
        'address_line2': '',
        'country': 'America',
        'city': 'New York',
        'region': 'NY',
        'postal_code': '10001'
    }
    response = requests.post(f'{BASE_URL}/register', json=registration_data)

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response content (if needed)
    # Example: assert response.json() == {'message': 'Registration successful'}

def test_success_page():
    # Test accessing the success page after form submission
    response = requests.get(f'{BASE_URL}/success')

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response content (if needed)
    # Example: assert 'Registration successful' in response.text
