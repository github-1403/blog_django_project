from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    ordering = ('title',)
    fields = ('title', 'text', 'status', 'author')


admin.site.register(Post, PostAdmin)
