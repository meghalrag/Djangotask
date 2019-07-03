from django.db import models

#Create your models here.
class LoginDB(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
class UserDB(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    dob=models.DateField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10,blank=False)
    city=models.CharField(max_length=100)
    qualification=models.CharField(max_length=10)
    FK_LoginDB=models.ForeignKey(LoginDB,on_delete=models.CASCADE)
    class Meta:
        db_table='usertable'