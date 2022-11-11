from rest_framework import status
import pytest


@pytest.mark.django_db
class TestRetrieveUser:
    def test_if_user_is_found_return_200(self, auth_client, user):
        response = auth_client.get(f'/users/{user.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == user.id
        assert response.data["username"] == user.username
        assert response.data["email"] == user.email
        assert response.data["bio"] == user.bio