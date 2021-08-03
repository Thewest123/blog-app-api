from django.contrib import admin
from blog import models


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_filter = ['is_for_logged_users_only', 'tags', 'category', 'author']
    search_fields = ['title', 'slug']


admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
