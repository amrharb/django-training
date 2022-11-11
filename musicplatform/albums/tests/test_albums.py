import pytest
from rest_framework import status
from artists.models import Artist
from artists.serializers import ArtistSerializer

@pytest.mark.django_db
class TestCreateAlbum:

    def test_if_albums_are_found_return_200(self, auth_client):
        response = auth_client.get('/albums/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_valid_returns_201(self, auth_client):
        artist = ArtistSerializer(data={"Stage_name":"khaled","Social_link":"https://www.ideone.com/"})
        artist.is_valid(raise_exception=True)
        artist.save()
        response = auth_client.post('/albums/',{"name":"album","release_at":"2020-02-02","cost":80,"artist":Artist.objects.filter(Stage_name="khaled")[0].id})
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_if_data_is_invalid_returns_400(self, auth_client):
        response = auth_client.post('/albums/',{})
        print(response.data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST