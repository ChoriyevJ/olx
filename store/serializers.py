from rest_framework import serializers

from store import models


class CategorySerializer(serializers.ModelSerializer):

    categories = serializers.JSONField()

    class Meta:
        model = models.Category
        fields = ('title', 'image', 'categories')


class CategoryPostSerializer(serializers.ModelSerializer):
    is_like = serializers.BooleanField()
    option = serializers.CharField()

    class Meta:
        model = models.Post
        fields = ('title', 'price', 'is_trade', 'address', 'created_at',
                  'is_like', 'option')


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = (
            'title', 'price', 'is_trade', 'description',
            'views', 'user',  'phone_number', 'address', 'is_like',
            'photos',
        )

