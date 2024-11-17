#query books by author
Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
#all books
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
#librarian
library = Library.objects.get(library=Library_name) 
librarian = library.librarian