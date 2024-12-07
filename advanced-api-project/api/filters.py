from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Partial matching for title
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Match author's name
    publication_year = filters.NumberFilter()  # Exact match for year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
