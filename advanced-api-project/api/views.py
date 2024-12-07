from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError

# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# View for Books
class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for Authors
class AuthorListCreateAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#second assignment and a better way

from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.generics import ListAPIView

from rest_framework.filters import SearchFilter, OrderingFilter



# ListView: Retrieve all books
# ListView: Open for everyone (read-only)

class BookListView(ListAPIView):
    # """
    # API view for listing books with filtering, searching, and ordering capabilities.
    # """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.AllowAny]  # Open to all users (read-only access)

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering setup
    filterset_class = BookFilter  # Allows filtering by title, author, and publication_year

    # Search setup
    search_fields = ['title', 'author__name']  # Enables search by book title or author's name

    # Ordering setup
    ordering_fields = ['title', 'publication_year', 'author__name']  # Fields users can order by
    ordering = ['title']  # Default ordering: alphabetical by title





# DetailView: Retrieve a single book by ID
# DetailView: Open for everyone (read-only)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open to all users (read-only access)

# CreateView: Add a new book 
# CreateView: Restricted to authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

    def perform_create(self, serializer):
        # Custom validation example: Ensure unique title per author
        title = serializer.validated_data.get('title')
        author = serializer.validated_data.get('author')
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({"detail": "This author already has a book with this title."})
        serializer.save()  # Save the book if validation passes


# UpdateView: Modify an existing book
# UpdateView: Restricted to authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
        # Example: Log the update action (can integrate with an actual logging system)
        instance = serializer.save()
        print(f"Book '{instance.title}' by {instance.author.name} was updated.")  # Replace with proper logging


# DeleteView: Remove a book
# DeleteView: Restricted to authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete




# from django_filters import rest_framework
# filters.OrderingFilter