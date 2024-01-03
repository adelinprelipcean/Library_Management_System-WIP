"""
URL configuration for my_library_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home'),
    path('books/', books_page, name='books'),
    path('your_bag/', your_bag, name='bag'),
    path('returns/', returns_page, name='returns'),
    path('login_page/', login_page, name='login_page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_book/', add_book, name='add_book'),
    path('delete_book/', delete_book_func, name='delete_book'),
    path('login_page/register', login_page, name='login_page'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
