from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from blog import models


class TagAndCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'slug']
    list_display = ['name', 'slug']
    ordering = ['name']


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title', 'slug']
    list_filter = ['is_for_logged_users_only', 'category', 'tags', 'author']
    list_display = ['title', 'category', 'author']
    readonly_fields = ['image_preview']
    date_hierarchy = 'publish_date'
    fieldsets = (
        (_('Blog post details'), {
            'fields': ['title', 'slug', 'author', 'category', 'content']
        }),
        (_('Image'), {
            'fields': ['image', 'image_preview']
        }),
        (_('Miscellaneous'), {
            'fields': ['is_for_logged_users_only', 'publish_date']
        }),
    )

    def image_preview(self, obj):
        if obj.image == '':
            return _("You haven't uploaded any image yet.")

        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" style="max-width: 30%; height:auto;" />'
            '</a>'
            .format(obj.image.url))


admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Category, TagAndCategoryAdmin)
admin.site.register(models.Tag, TagAndCategoryAdmin)
