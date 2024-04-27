import requests
import pytest

BASE_URL = 'http://example.com'  # Replace with your base URL

def test_response_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_response_time():
    response = requests.get(BASE_URL)
    assert response.elapsed.total_seconds() * 1000 < 200

def test_response_contains_expected_html_elements_and_classes():
    response = requests.get(BASE_URL)
    assert '<div class="container mt-5">' in response.text
    assert '<div class="alert alert-success" role="alert">' in response.text
    assert '<a href="index.html" class="btn btn-primary">Return to Registration</a>' in response.text

def test_verify_return_to_registration_button_presence_and_url():
    response = requests.get(BASE_URL)
    assert 'href="index.html"' in response.text
    assert 'Return to Registration' in response.text

if __name__ == '__main__':
    pytest.main(['-v', '--capture=no'])
