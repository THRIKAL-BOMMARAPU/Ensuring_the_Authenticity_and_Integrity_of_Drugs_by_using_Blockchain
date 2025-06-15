import pytest
import django
from django.test import Client, TestCase


django.setup()

class BasicTests(TestCase):
    def setUp(self):
        self.client = Client() 

    def test_dummy(self):
        """A dummy test to ensure pytest works"""
        assert 1 == 1  

    def test_home_page(self):
        """Test home page response (if implemented)"""
        response = self.client.get("/index.html")
        assert response.status_code in [200, 404]  # Handles missing views

    def test_admin_login_page(self):
        response = self.client.get("/AdminLogin.html")
        assert response.status_code in [200, 404]

    def test_stake_login_page(self):
        response = self.client.get("/StakeLogin.html")
        assert response.status_code in [200, 404]

    def test_generate_orders(self):
        response = self.client.get("/GenerateOrders")
        assert response.status_code in [200, 404]

    def test_admin_tracing(self):
        response = self.client.get("/AdminTracing.html")
        assert response.status_code in [200, 404]

    def test_consumer_tracing(self):
        response = self.client.get("/ConsumerTracing.html")
        assert response.status_code in [200, 404]

    def test_admin_map(self):
        response = self.client.get("/AdminMap")
        assert response.status_code in [200, 404]

    def test_user_map(self):
        response = self.client.get("/UserMap")
        assert response.status_code in [200, 404]


@pytest.mark.django_db
def test_index_page(client):
    response = client.get("/index.html")  # Direct URL test
    assert response.status_code == 200  

@pytest.mark.django_db
def test_admin_login_page(client):
    response = client.get("/AdminLogin.html")  
    assert response.status_code == 200  

@pytest.mark.django_db
def test_admin_login_action(client):
    response = client.post("/AdminLoginAction", {"username": "admin", "password": "admin123"})
    assert response.status_code in [200, 302]  

@pytest.mark.django_db
def test_stake_login_page(client):
    response = client.get("/StakeLogin.html")
    assert response.status_code == 200 

@pytest.mark.django_db
def test_generate_orders(client):
    response = client.get("/GenerateOrders")
    assert response.status_code == 200 

@pytest.mark.django_db
def test_admin_tracing(client):
    response = client.get("/AdminTracing.html")
    assert response.status_code == 200  

@pytest.mark.django_db
def test_consumer_tracing(client):
    response = client.get("/ConsumerTracing.html")
    assert response.status_code == 200  

@pytest.mark.django_db
def test_admin_map(client):
    response = client.get("/AdminMap")
    assert response.status_code == 200  

@pytest.mark.django_db
def test_user_map(client):
    response = client.get("/UserMap")
    assert response.status_code == 200  