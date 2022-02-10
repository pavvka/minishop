from rest_framework import serializers

from .models import Category, Product, ProductComment

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = [
            'id',
            'user',
            'text',
            'created_date',
        ]

class ProductSerializer(serializers.ModelSerializer):
    comments = ProductCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            'comments'
        ]

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )