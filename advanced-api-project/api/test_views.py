from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create sample data
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Sample Book", publication_year=2022, author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        self.client.force_authenticate(user=self.user)  # Authenticate if needed
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {"title": "Updated Book"}
        self.client.force_authenticate(user=self.user)  # Authenticate if needed
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)  # Authenticate if needed
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Sample")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_order_books_by_title(self):
        Book.objects.create(title="Another Book", publication_year=2021, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=title")
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ["Another Book", "Sample Book"])
