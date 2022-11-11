import pytest
from rest_framework import status

@pytest.mark.django_db
class TestCreateArtist:
    def test_if_artists_are_found_return_200(self, auth_client):
        response = auth_client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK
    
    def test_if_data_is_valid_returns_201(self, auth_client):
        response = auth_client.post('/artists/',{"Stage_name":"afdkladfjdk","Social_link":"https://www.ideone.com/"})
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_if_data_is_invalid_returns_400(self, auth_client):
        response = auth_client.post('/artists/',{})
        assert response.status_code == status.HTTP_400_BAD_REQUEST