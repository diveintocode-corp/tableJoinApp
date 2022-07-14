from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserList(ListView):
    model = User
    template_name = "accounts/index.html"
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:index')


class UserDetail(DetailView):
    model = User
    template_name = "accounts/detail.html"
    context_object_name = 'user'
