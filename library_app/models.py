from django.db import models
from django import forms
from django.core.validators import MinValueValidator 

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  
    publisher = models.CharField(max_length=100)   
    cover = models.ImageField(upload_to='', null=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    def __str__(self):
        return f"{self.title} has id {self.id}, author as {self.author}, publisher as {self.publisher} and the available quantity is {self.quantity}"
    
    
