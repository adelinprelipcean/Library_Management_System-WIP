from django.db import models

# Create your models here.
class reader(models.Model):
    reference_id = models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_adress = models.TextField()
    confirmed = models.BooleanField(default=False)
    