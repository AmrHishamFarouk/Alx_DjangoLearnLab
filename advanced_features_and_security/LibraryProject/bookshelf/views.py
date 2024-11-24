from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post, Book
from django.http import HttpResponseForbidden
from .forms import BookSearchForm

# View to create a post
@permission_required('app_name.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        return redirect('post_list')
    return render(request, 'create_post.html')

# View to edit a post
@permission_required('app_name.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'edit_post.html', {'post': post})

# View to delete a post
@permission_required('app_name.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')

# View to view a post (optional permission)
@permission_required('app_name.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})



# View to list all books (requires 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books in the bookshelf.
    Only users with 'can_view' permission can access this page.
    """
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_search(request):
    # Handle GET requests and initialize the form
    if request.method == "GET":
        form = BookSearchForm(request.GET)  # Pass GET parameters to the form
        if form.is_valid():
            # If the form is valid, use the cleaned query to filter books
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)  # Search books by title
        else:
            # If no valid query, display all books
            books = Book.objects.all()
    else:
        books = Book.objects.all()  # Display all books if the request isn't GET
    
    # Return the context with books and form
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
