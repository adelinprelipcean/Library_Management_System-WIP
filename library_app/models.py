from django.db import models
from django import forms

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  
    publisher = models.CharField(max_length=100)   
    cover = models.ImageField(upload_to='', null=True)
    def __str__(self):
        return f"{self.title} has id {self.id}, author as {self.author} and publisher as {self.publisher}"
    
    
