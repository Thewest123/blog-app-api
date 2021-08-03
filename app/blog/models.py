import os
import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


UNCATEGORIZED_CATEGORY_ID = 1


def blog_image_file_path(instance, filename):
    """Generates file path for newly uploaded blog image"""
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join('uploads/blog/', filename)


class BlogPost(models.Model):
    """Model for the Blog Post"""

    title = models.CharField(max_length=80)

    slug = models.SlugField()

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_DEFAULT,
        default=UNCATEGORIZED_CATEGORY_ID)

    tags = models.ManyToManyField('Tag', blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    image = models.ImageField(
        null=True,
        upload_to=blog_image_file_path,
        blank=True
    )

    is_for_logged_users_only = models.BooleanField(
        default=False,
        help_text=_('When selected, only logged-in users can '
                    'view this post or see it in posts list')
    )

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
