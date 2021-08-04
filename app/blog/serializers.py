from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import BlogPost, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name']


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for the BlogPost list view"""

    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'category', 'tags', 'author']


class BlogPostDetailSerializer(BlogPostSerializer):
    """Serializer for the BlogPost detail view"""

    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'
