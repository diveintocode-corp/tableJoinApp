from django.urls import path
from django.views.generic import ListView, CreateView, DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

app_name = 'accounts'

urlpatterns = [
    path('', ListView.as_view(
        template_name='accounts/index.html',
        model=User,
        context_object_name='users',
    ), name='index'),
    path('signup/', CreateView.as_view(
        template_name='accounts/signup.html',
        form_class=CustomUserCreationForm,
        success_url='/accounts',
    ), name='signup'),
    path('user_detail/<int:pk>/', DetailView.as_view(
        model=User,
        template_name='accounts/detail.html',
        context_object_name='user',
    ), name='detail')
]
