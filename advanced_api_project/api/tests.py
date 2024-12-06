#note this is not needed as we are using APITestCase
from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class APITest(APITestCase):
    def test_create_book(self):
        author = Author.objects.create(name="Test Author")
        data = {
            "title": "Test Book",
            "publication_year": 2023,
            "author": author.id
        }
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Book")

    def test_invalid_publication_year(self):
        author = Author.objects.create(name="Test Author")
        data = {
            "title": "Future Book",
            "publication_year": 2025,  # Invalid year
            "author": author.id
        }
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("publication_year", response.data)

    def test_get_authors_with_books(self):
        author = Author.objects.create(name="Test Author")
        Book.objects.create(title="Book 1", publication_year=2000, author=author)
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]["books"]), 1)

