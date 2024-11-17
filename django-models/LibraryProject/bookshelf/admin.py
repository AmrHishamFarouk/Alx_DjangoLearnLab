from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('publication_year',)  # Filters to apply on the right side

admin.site.register(Book, BookAdmin)