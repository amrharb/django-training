from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ArtistSerializer
from rest_framework.permissions import AllowAny
from .models import Artist

class ArtistsView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.validated_data,status=status.HTTP_201_CREATED)