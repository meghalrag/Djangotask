from django.shortcuts import render,HttpResponse,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection,IntegrityError
from django.contrib import messages
from .forms import RegForm,LoginForm
from .models import UserDB,LoginDB
# from util.db import to_dict
# Create your views here.
def home(request):
    obj=UserDB.objects.all()
    return render(request,'reg.html',{'obj':obj})
def loginfunc(request):
    if request.method=='POST':
        forms=LoginForm(request.POST)
        if forms.is_valid():
            uname=forms.cleaned_data['username']
            passw=forms.cleaned_data['password']
            try:
                obj=LoginDB.objects.get(username=uname,password=passw)
                request.session['id']=obj.id
                return redirect('user:userhome')
            except ObjectDoesNotExist:
                messages.add_message(
                request,
                messages.ERROR,
                'userrname or password incorrect'
                )
                return redirect('user:login')
    else:
        forms=LoginForm() 
        return render(request,'create.html',{'f':'login','form':forms})
def userhome(request):
    obj=UserDB.objects.all()
    return render(request,'home.html',{'obj':obj,'userid':request.session['id']})
def createfunc(request):
    
    if request.method=="POST":
        forms=RegForm(request.POST)
        if forms.is_valid():
            uname=forms.cleaned_data['usernamereg']
            passw=forms.cleaned_data['passwordreg']
            cpassw=forms.cleaned_data['cpasswordreg']
            if passw != cpassw:
                messages.add_message(
                request,
                messages.ERROR,
                'password not match'
                )
                return redirect('user:create')
            name=forms.cleaned_data['name']
            email=forms.cleaned_data['email']
            mob=forms.cleaned_data['Mobile_Number']
            dob=forms.cleaned_data['dob']
            gender=forms.cleaned_data['Gender']
            city=forms.cleaned_data['city']
            qualifi=forms.cleaned_data['qualification']
            # return render(request,'create.html',{'form':forms})
            try:
                obj=LoginDB(username=uname,password=passw)
                obj.save()
                obj2=UserDB(name=name,email=email,dob=dob,phone=mob,gender=gender,city=city,qualification=qualifi,FK_LoginDB=obj)
                obj2.save()
                messages.add_message(
                request,
                messages.SUCCESS,
                'Student added successfully'
                
            )
                return redirect('user:home')
            except IntegrityError as e:
                messages.add_message(
                request,
                messages.ERROR,
                'username alraedy exists'
            )
            return redirect('user:create')
        else:
             for error_field in forms.errors:
                if error_field in forms.fields:
                    forms.fields[error_field].widget.attrs['class'] += ' is-invalid'
            # return HttpResponse(forms.errors)
    else:
        forms=RegForm()
    return render(request,'create.html',{'form':forms})
def logoutfunc(request):
    del request.session['id']
    return redirect('user:home')
def deletefunc(request,user_id):
    obj=LoginDB.objects.get(id=request.session['id'])
    # obj=UserDB.objects.get(id=user_id)
    obj.delete()
    
    messages.add_message(
                request,
                messages.SUCCESS,
                'Student deleted successfully'
            )
    return (logoutfunc(request))
def editfunc(request,user_id):
    obj=UserDB.objects.get(id=user_id)
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        city=request.POST['city']
        obj=UserDB.objects.filter(id=user_id).update(name=name,phone=phone,city=city)
        messages.add_message(
                request,
                messages.SUCCESS,
                'Student updated successfully'
            )
        return userhome(request)
    return render(request,'update.html',{'obj':obj,'userid':user_id})
    # form = RegForm(request.POST or None,instance=obj)
    # return render(request,'create.html',{'form':form})
def viewfunc(request,user_id):
    # Executing raw sql queries
    objlog=UserDB.objects.get(id=user_id)
    cursor=connection.cursor()
    cursor.execute("select name,email,gender,city,phone,qualification,dob from usertable where id=%s",[user_id])
    rs=cursor.fetchone()
    li=['name','email','gender','city','phone','qualification','dob']
    zipobj=zip(li,rs)
    obj=dict(zipobj)
    if objlog.FK_LoginDB.id==request.session['id']:
        obj['username']=objlog.FK_LoginDB.username
        obj['password']=objlog.FK_LoginDB.password
    else:
        obj['username']='it is not visible'
        obj['password']='it is not visible'
    #converting to dict
    # obj=to_dict(cursor,rs)

    return render(request,'view.html',{'obj':obj})
    
