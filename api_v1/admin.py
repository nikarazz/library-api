from django.contrib import admin
from .models import Author, Genre, Book, Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date']
    search_fields = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published_date', 'created_at']
    list_filter = ['author', 'genres', 'published_date']
    search_fields = ['title', 'description']
    filter_horizontal = ['genres']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'text_preview', 'created_at', 'user']
    list_filter = ['book', 'created_at']
    search_fields = ['text']

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Текст комментария'