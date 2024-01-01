from django.db import models

# Create your models here.
class User():
    is_admin = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  
    publisher = models.CharField(max_length=100)   
    cover = models.ImageField(upload_to='library_app/covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.cover.delete()