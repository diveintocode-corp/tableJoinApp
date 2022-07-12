from django.urls import path
from . import views
app_name = 'variations'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:variation_id>', views.detail, name='detail'),
    path('edit/<int:variation_id>', views.edit, name='edit'),
    path('delete/<int:variation_id>', views.delete, name='delete'),
]
