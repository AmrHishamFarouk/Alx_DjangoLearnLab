# Custom Permissions and Groups in Django

## Custom Permissions:
1. **can_view**: Allows the user to view a post.
2. **can_create**: Allows the user to create a post.
3. **can_edit**: Allows the user to edit a post.
4. **can_delete**: Allows the user to delete a post.

## Groups:
- **Editors**: Has `can_create` and `can_edit` permissions.
- **Viewers**: Has only the `can_view` permission.
- **Admins**: Has `can_create`, `can_edit`, `can_delete`, and `can_view` permissions.

## How to Use:
1. Create groups via the Django Admin interface.
2. Assign custom permissions to the groups.
3. Assign users to the appropriate groups.
4. Use the `@permission_required` decorator in your views to enforce these permissions.

Make sure to test the permissions by logging in as users from different groups and verifying their access rights.
