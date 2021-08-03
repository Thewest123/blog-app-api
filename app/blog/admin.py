from django.contrib import admin
from blog import models


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
