#query books by author
author = Author.objects.get(name=author_name)
books_by_author = author.books.all() 
#all books
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
#librarian
library = Library.objects.get(name=Library_name) 
librarian = library.librarian