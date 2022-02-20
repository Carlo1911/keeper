from django.contrib import admin

from .models import WebBookmark


@admin.register(WebBookmark)
class WebBookmarkAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = (
        'title',
        'public',
        'user',
    )
