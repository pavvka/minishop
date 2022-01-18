from django.shortcuts import render
from rest_framework.views import APIView

from .models import Employee

class UserDetails(APIView):
    def get_object(self, request):
        try:
            return Employee.objects.filter(user=request.user)
        except Employee.DoesNotExist:
            raise
