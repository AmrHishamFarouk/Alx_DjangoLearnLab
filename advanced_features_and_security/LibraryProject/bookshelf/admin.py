from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Book,CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('publication_year',)  # Filters to apply on the right side

admin.site.register(Book, BookAdmin)

# Define the custom admin for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'date_of_birth']
    search_fields = ['email', 'username']
    ordering = ['email']

    # Fields to be displayed in the admin form for editing users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'date_of_birth', 'profile_photo')}),
    )
    # Ensure that 'email' is set as the username field
    required_fields = ['email']

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
