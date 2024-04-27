from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)  # Set the waiting time between requests

    @task
    def index(self):
        self.client.get("/")

    @task
    def register(self):
        # Define sample registration data
        registration_data = {
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'birth_date': '1990-01-01',
            'gender': 'Male',
            'address_line1': '123 Main Street',
            'address_line2': 'Apt 4B',
            'country': 'United States',
            'city': 'New York',
            'region': 'NY',
            'postal_code': '10001'
        }
        # Send a POST request to register
        self.client.post("/register", json=registration_data)

    @task
    def success(self):
        self.client.get("/success")
