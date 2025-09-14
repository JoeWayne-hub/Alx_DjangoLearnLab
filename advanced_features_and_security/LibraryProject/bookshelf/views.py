from django.shortcuts import render

# Create your views here.
# bookshelf/views.py
from django.shortcuts import render
from .models import Book
from django.db.models import Q

def book_search(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        #  Safe ORM query
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    return render(request, "bookshelf/book_list.html", {"results": results, "query": query})
