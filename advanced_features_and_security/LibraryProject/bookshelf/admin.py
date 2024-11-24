from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Book,CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('publication_year',)  # Filters to apply on the right side

admin.site.register(Book, BookAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
