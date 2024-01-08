from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Book
from .forms import *

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
          quantity = request.POST['quantity']
          cover = request.POST['cover']
          Book.objects.create(title=title, author=author, publisher=publisher, quantity=quantity, cover=cover)
          return redirect(reverse('delete_book'))
     return render(request,'books/add_book.html', context)

def upload_image(request): 
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("add_book")
    else:
        form = BookForm()
        context = {
            'form': form
        }
    return render(request, 'books/add_book.html', context)

def delete_book_func(request):
     book = Book.objects.all()
     context={'book': book}
     return render(request, 'books/delete_book.html',context)

def delete_event(request, event_id):
     event = Book.objects.get(pk=event_id)
     event.delete()
     return redirect('delete_book')

def update_book_func(request, event_id):
     book = Book.objects.get(pk=event_id)
     context={'book': book}
     return render(request, 'books/edit_book.html',context)

def edit_book(request, book_id):
     book = get_object_or_404(Book, id=book_id)
     if request.method == 'POST':
          form = EditBookForm(request.POST)
          if form.is_valid():
               book.quantity = form.cleaned_data['quantity']
               book.save()
               return redirect('delete_book')
     else:
          form = EditBookForm(initial={'quantity': book.quantity})

     return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)

    context = {
        'books': books,
    }

    return render(request, 'books/book_list.html', context)
