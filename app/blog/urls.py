from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views


router = DefaultRouter()
router.register("posts", views.BlogPostViewSet)
router.register("authors", views.UserViewSet)
router.register("categories", views.CategoryViewSet)
router.register("tags", views.TagViewSet)

app_name = "blog"

urlpatterns = [
    path("", include(router.urls))
]
