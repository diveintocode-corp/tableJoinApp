from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('', views.UserList.as_view(), name='index'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='detail')
]
