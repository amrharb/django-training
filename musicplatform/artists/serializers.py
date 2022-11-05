from rest_framework import serializers
from .models import Artist
from albums.models import Album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    albums =  AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['Stage_name','Social_link', 'albums']
