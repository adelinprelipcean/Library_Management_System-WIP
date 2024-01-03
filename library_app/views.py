from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse

# Create your views here.

def home_page(request):
     return render(request,'home.html', context={"current_tab": "home"})

def books_page(request):
     book = Book.objects.all()
     context={'book': book}
     return render(request,'books.html', context)

def your_bag(request):
     return render(request,'your_bag.html', context={"current_tab": "your_bag"})

def returns_page(request):
     return render(request,'returns.html', context={"current_tab": "returns"})

def login_page(request):
     return render(request,'login_page.html', context={"current_tab": "login_page"})

def register_page(request):
     return render(request,'register.html', context={"current_tab": "login_page"})

def dashboard(request):
     book = Book.objects.all()
     context={'book': book}
     return render(request,'dashboard.html', context)

def add_book(request):
     book = Book.objects.all()
     context={'book': book}
     if request.POST:
          title = request.POST['title']
          author = request.POST['author']
          publisher = request.POST['publisher']
          Book.objects.create(title=title, author=author, publisher=publisher)
          return redirect(reverse('delete_book'))
     return render(request,'books/add.html', context)

def delete_book_func(request):
     book = Book.objects.all()
     context={'book': book}
     
     if request.POST:
          title = request.POST['title']
          try:
               Book.objects.get(title=title).delete()
               return redirect(reverse('delete_book'))
          except:
               print('Title not found!')
               return redirect(reverse('delete_book'))
     else:
          return render(request, 'books/delete.html',context)

