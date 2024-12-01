from django.urls import path, include
from .views import BookList, BookViewSet

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

# Create the router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet
    path('', include(router.urls)),  # Includes all CRUD routes registered with the router

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication URL
]
