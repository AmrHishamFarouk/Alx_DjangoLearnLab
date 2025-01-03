from django.urls import path
from .views import UserCreate, CustomAuthToken,FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('users/', UserListView.as_view(), name='user-list'),
]
