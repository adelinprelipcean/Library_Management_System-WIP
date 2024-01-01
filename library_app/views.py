from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import User
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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