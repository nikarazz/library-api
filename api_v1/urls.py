from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, GenreViewSet, BookViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'books', BookViewSet, basename='book')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]