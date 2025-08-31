book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
 "from bookshelf.models import Book"
# Expected Output: <QuerySet []>
