from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home_page(request):
     return render(request,'home.html', context={"current_tab": "home"})

def books_page(request):
     return render(request,'books.html', context={"current_tab": "books"})

def your_bag(request):
     return render(request,'your_bag.html', context={"current_tab": "your_bag"})

def returns_page(request):
     return render(request,'returns.html', context={"current_tab": "returns"})

def login_page(request):
     return render(request,'login_page.html', context={"current_tab": "login_page"})