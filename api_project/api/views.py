from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

from rest_framework import viewsets

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#  generics.ListAPIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
