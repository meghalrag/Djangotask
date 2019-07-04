from django.shortcuts import render,HttpResponse
import json
from .models import Mydb
# Create your views here.
def home(request):
    if request.method=='POST':
       email=request.POST['email']
       passw=request.POST['passw']
       obj=Mydb(email=email,passwod=passw)
      #  obj.save()
       return render(request,'sample.html',{})
    return render(request,'home.html',{})
def getajax(request):
   # obj={'email':'haiiiiii','name':'akash','age':20,'gender':'male'}
   obj=Mydb.objects.get(passwod=12345)
   mydict={'email':obj.email}
   obj=json.dumps(mydict)
   return HttpResponse(obj)