#query books by author
books_by_author = Book.objects.filter(author=author)
#all books
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
#librarian
library = Library.objects.get(name=Library_name) 
librarian = library.librarian