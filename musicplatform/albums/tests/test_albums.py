import pytest
from rest_framework import status

@pytest.mark.django_db
class TestCreateAlbum:

    def test_if_albums_are_found_return_200(self, auth_client):
        response = auth_client.get('/albums/albums/')
        assert response.status_code == status.HTTP_200_OK