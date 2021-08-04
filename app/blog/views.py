from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins

from blog.models import BlogPost, Category, Tag
from blog import serializers


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = BlogPost.objects.all()
    lookup_field = 'slug'

    serializer_classes = {
        'list': serializers.BlogPostSerializer,
        'retrieve': serializers.BlogPostDetailSerializer,
    }
    default_serializer_class = serializers.BlogPostSerializer

    def get_serializer_class(self):
        """Set the serializer class based on action"""
        return self.serializer_classes.get(
            self.action,
            self.default_serializer_class
        )

    def get_queryset(self):
        """Filter the results based on query parameters and auth"""
        queryset = self.queryset

        # Hide BlogPosts that have is_for_logged_users_only=True
        # if user is not authenticated
        if not self.request.user.is_authenticated:
            queryset = queryset.exclude(is_for_logged_users_only=True)

        # Get query params and filter the queryset
        author = self.request.query_params.get('author')
        category = self.request.query_params.get('category')
        tags = self.request.query_params.get('tags')

        if author:
            queryset = queryset.filter(author__id__exact=int(author))

        if category:
            queryset = queryset.filter(category__slug__exact=category)

        if tags:
            tags_list = tags.split(',')
            queryset = queryset.filter(tags__slug__in=tags_list).distinct()

        return queryset.order_by('title')


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin):

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin):

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
