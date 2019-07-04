from django.db import models

# Create your models here.
class Mydb(models.Model):
    email=models.CharField(max_length=50,null=True)
    passwod=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50,null=True)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=50,null=True)
    class Meta:
        db_table='mytable'