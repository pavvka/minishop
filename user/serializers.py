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

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'city', 'date_of_birth')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if CustomUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if CustomUser.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.city = validated_data['city']
        instance.email = validated_data['email']
        instance.date_of_birth = validated_data['date_of_birth']

        instance.save()

        return instance