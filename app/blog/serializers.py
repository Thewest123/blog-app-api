from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import BlogPost, Category, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name', 'slug']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'slug']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name']


class BlogPostSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'category', 'tags', 'author']


class BlogPostDetailSerializer(BlogPostSerializer):

    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'
