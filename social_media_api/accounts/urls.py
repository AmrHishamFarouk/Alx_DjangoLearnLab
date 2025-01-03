from django.urls import path
from .views import UserCreate, CustomAuthToken,follow_user, unfollow_user

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
