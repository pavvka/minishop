from rest_framework import serializers

from .models import Category, Product, ProductComment

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = [
            'id',
            'author',
            'text',
            'created_date',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "comments",
            "get_image",
            "get_thumbnail"
        )
    def get_pagecomment_set(self, instance):

        page_comment = instance.comments.all()
        return ProductCommentSerializer(page_comment, many=True).data

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