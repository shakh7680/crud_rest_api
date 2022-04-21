from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['author', 'body', 'created_at', 'updated_at', 'title']