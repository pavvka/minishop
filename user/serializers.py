from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):   
    date_of_birth = serializers.SerializerMethodField('date_of_birth') 
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            'username',
            "city",
            "date_of_birth"
        )