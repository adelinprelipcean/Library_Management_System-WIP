from django.db import models
from django import forms
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  
    publisher = models.CharField(max_length=100)   

    def __str__(self):
        return self.title
