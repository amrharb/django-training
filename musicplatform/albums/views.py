from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer
from rest_framework import status
from .models import Album
from rest_framework.permissions import AllowAny
class AlbumView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        serializer = AlbumSerializer(Album.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)