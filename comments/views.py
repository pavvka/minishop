from django.shortcuts import render

from .models import Comment
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CommentSerializer
from .models import Comment
from django.http import Http404

class CommentList(APIView):
    def get_object(self, product_slug):
        try:
            return Comment.objects.get(slug=product_slug)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self, request, product_slug, format=None):
        comments = self.get_object(product_slug)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
