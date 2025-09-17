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
from .forms import ExampleForm

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Normally, process the data here
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # Just return success page or re-render form with message
            return render(request, "bookshelf/form_example.html", {"form": form, "success": True})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})