from django.urls import path
from .views import BookListCreateAPIView, AuthorListCreateAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
]
