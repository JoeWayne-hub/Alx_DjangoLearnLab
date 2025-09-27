from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create Author and Books
        self.author = Author.objects.create(name="Author One")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

        # API endpoints
        self.list_url = reverse("book-list")   # /books/
        self.detail_url = reverse("book-detail", args=[self.book1.id])  # /books/<id>/

    # Test GET (ListView)
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Book One", str(response.data))

    # Test GET (DetailView)
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # Test POST (CreateView)
    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # Test PUT (UpdateView)
    def test_update_book(self):
        data = {"title": "Updated Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # Test DELETE (DeleteView)
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Test Search
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Book One", str(response.data))

    # Test Ordering
    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book Two")

    # Test Filtering
    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url + "?publication_year=2020")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

    # Test Permissions (unauthenticated user should not create)
    def test_unauthenticated_user_cannot_create(self):
        unauth_client = APIClient()
        data = {"title": "Forbidden Book", "publication_year": 2022, "author": self.author.id}
        response = unauth_client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
