from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer
from .models import Artist
class ArtistsView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Artist.objects.create(serializer)
        return Response(serializer.validated_data)
