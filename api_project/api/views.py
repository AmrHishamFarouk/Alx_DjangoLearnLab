from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser   # Import IsAuthenticated permission

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Apply permissions
    permission_classes = [IsAuthenticated]   # Ensure only authenticated users can access the API

#  generics.ListAPIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow only authenticated users to access
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:  # Actions that require admin access
            permission_classes = [IsAdminUser]
        else:  # Read actions (list, retrieve)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
