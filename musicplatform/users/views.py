from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
class UserDetailView(APIView):
    permission_classes = [AllowAny]

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)

    def post(self,request):
        user = get_object_or_404(User)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)