from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    path('variations/', include('variations.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
