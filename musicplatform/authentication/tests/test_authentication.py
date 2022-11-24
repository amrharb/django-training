import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCreateRegister:
    def test_if_data_is_valid_return_201(self, auth_client):
        user = {
            "username": "AmrHarb", 
            "email": "amr@gmail.com",
            "password1": "22222222", 
            "password2": "22222222"
        }
        response = auth_client.post('/authentication/register/', user)
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, auth_client):
        user = {}
        response = auth_client.post('/authentication/register/', user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogin:
    def test_if_data_is_ok_return_200(self, auth_client):
        user = {
            "username": "AmrHarb", 
            "email": "amr@gmail.com",
            "password1": "22222222", 
            "password2": "22222222"
        }
        auth_client.post(
            '/authentication/register/', user)
        response = auth_client.post(
            '/authentication/login/', {"username": "AmrHarb", "password": "22222222"})
        assert response.status_code == status.HTTP_202_ACCEPTED

    def test_if_data_is_invalid_return_400(self, auth_client):
        user = {
            "username": "AmrHarb", 
            "email": "amr@gmail.com",
            "password1": "22222222", 
            "password2": "22222222"
        }
        auth_client.post(
            '/authentication/register/', user)
        response = auth_client.post('/authentication/login/',
                                    {"username": "Amr"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogout:
    def test_if_no_content_return_204(self, auth_client):
        response = auth_client.post('/authentication/logout/')
        assert response.status_code == status.HTTP_204_NO_CONTENT