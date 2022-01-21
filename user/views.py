from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserDetails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = CustomUser.objects.filter(user=request.user)
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)
