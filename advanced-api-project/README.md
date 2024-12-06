# Book API

This API allows users to perform CRUD operations on Book instances, which include creating, updating, deleting, and retrieving books. The API is built using Django REST Framework.

## Views Overview

The views in this project follow the standard DRF class-based views, extended to include custom logic for each operation where necessary. Below is an overview of each view.

### 1. **BookListView (GET /books/)**
- **Purpose**: Retrieves a list of all books.
- **Authentication**: No authentication is required. This view is open to all users.
- **Customizations**: 
  - Allows filtering by author through the query parameter `author`.
  
### 2. **BookDetailView (GET /books/{id}/)**
- **Purpose**: Retrieves details of a single book by its ID.
- **Authentication**: No authentication is required. This view is open to all users.

### 3. **BookCreateView (POST /books/create/)**
- **Purpose**: Creates a new book instance.
- **Authentication**: Requires the user to be authenticated.
- **Customizations**:
  - The `perform_create` method allows additional logic before saving the book, such as associating the current authenticated user with the book.

### 4. **BookUpdateView (PUT /books/{id}/update/)**
- **Purpose**: Updates an existing book instance.
- **Authentication**: Requires the user to be authenticated.
- **Customizations**:
  - The `perform_update` method allows performing extra logic before saving the updated book instance.

### 5. **BookDeleteView (DELETE /books/{id}/delete/)**
- **Purpose**: Deletes an existing book instance.
- **Authentication**: Requires the user to be authenticated.
- **Customizations**:
  - The `perform_destroy` method provides a hook to add extra logic before the book is deleted.

## Permissions

- **`IsAuthenticated`**: The views `BookCreateView`, `BookUpdateView`, and `BookDeleteView` require users to be authenticated.
- **Read-Only Access**: `BookListView` and `BookDetailView` are available to both authenticated and unauthenticated users.

## Testing with Postman

- **For GET requests (List and Detail views)**: No authentication is required.
- **For POST, PUT, and DELETE requests (Create, Update, and Delete views)**: You need to authenticate using token-based authentication. Ensure to include `Authorization: Token <your_token>` in the request headers.

Example:
```bash
Authorization: Token <your_token>
