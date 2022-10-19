from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtistSerializer
from .models import Artist
class ArtistsView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)