from random import randint
from .models import Album, Song
from artists.models import Artist
from rest_framework import serializers
from artists.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_at', 'cost']
        artist = ArtistSerializer(read_only=True)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'album', 'name',  'image', 'audio']
    album = AlbumSerializer()