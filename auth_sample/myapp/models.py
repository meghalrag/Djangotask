from django.db import models

# Create your models here.
class MyDB(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    passw=models.CharField(max_length=50)