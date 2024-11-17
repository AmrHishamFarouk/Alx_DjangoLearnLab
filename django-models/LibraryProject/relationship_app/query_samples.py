#query books by author
books_by_author = Books.object.all().filter(author__name='author_name')
#all books
books = Books.objects.all().filter(library__name='library_name')
#librarian
librarian = librarian.objects.all().filter(library__name='library_name')
