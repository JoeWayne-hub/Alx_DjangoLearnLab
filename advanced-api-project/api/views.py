from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.utils import timezone
from .models import Book
from .serializers import BookSerializer

# 📖 List all books (anyone can view)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public read access

# 📖 Retrieve one book by ID (anyone can view)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public read access

# ➕ Create a book (only authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior on create
    def perform_create(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        if publication_year and publication_year > timezone.now().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()

# ✏️ Update a book (only authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior on update
    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        if publication_year and publication_year > timezone.now().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()

# ❌ Delete a book (only authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
