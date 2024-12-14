from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms

# Registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Registration view
class RegisterView(CreateView):
    template_name = 'blog/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

# Profile view
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'blog/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
