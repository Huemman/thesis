from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'department')
    search_fields = ['title', 'abstract', 'authors']

admin.site.register(Post, PostAdmin)
