from django.shortcuts import render

from .models import Comment
from rest_framework.response import Response
from rest_framework.views import APIView

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Comment.objects.all()
        #serializer = ProductSerializer(products, many=True)
        return Response(products)
