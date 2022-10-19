from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer
from rest_framework import status
class AlbumView(APIView):
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status=status.HTTP_201_CREATED)