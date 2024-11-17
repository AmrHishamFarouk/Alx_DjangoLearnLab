from django.shortcuts import render
from django.http import HttpResponse
from relationship_app.models import Book
from django.views.generic.detail import DetailView
from relationship_app.models import Library
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
    
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Custom template
    context_object_name = "library"  # Name for the context variable in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books in the library to the context
        context['books'] = self.object.books.all()  # Access related books
        return context