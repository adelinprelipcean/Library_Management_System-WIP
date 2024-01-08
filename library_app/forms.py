from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('id','title', 'author', 'publisher', 'quantity', 'cover')

class EditBookForm(forms.Form):
        quantity = forms.IntegerField(label='New Quantity')