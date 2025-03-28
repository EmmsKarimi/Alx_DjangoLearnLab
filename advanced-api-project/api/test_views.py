from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    """
    Test case for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Fantastic Beasts", publication_year=2016, author=self.author)

        # Authenticated client
        self.client.force_authenticate(user=self.user)

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """
        Test retrieving a single book.
        """
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {"title": "The Casual Vacancy", "publication_year": 2012, "author": self.author.id}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """
        Test updating a book.
        """
        data = {"title": "Harry Potter and the Sorcerer's Stone", "publication_year": 1997, "author": self.author.id}
        response = self.client.put(f"/api/books/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter and the Sorcerer's Stone")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        response = self.client.get("/api/books/?title=Harry Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get("/api/books/?search=Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harry Potter")  # Older book should come first
