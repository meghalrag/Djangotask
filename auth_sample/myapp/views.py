from django.shortcuts import render,HttpResponse,redirect
from .forms import MyForm,LoginForm
from .models import MyDB
# Create your views here.
def homefunc(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            usern=form.cleaned_data['usern']
            passw=form.cleaned_data['passw']
            obj=MyDB.objects.all()
            for i in obj:
                if i.username==usern and i.passw==passw:
                    request.session['id']=i.id
                    return render(request,'home.html',{'userid':request.session['id']})
            return HttpResponse('cannot login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def myfunc(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            form.clean()
            usern=form.cleaned_data['username']
            email=form.cleaned_data['email']
            passw=form.cleaned_data['passw']
            cpassw=form.cleaned_data['confirmpassw']
            if passw !=cpassw:
                return HttpResponse('password not match')
            else:
                form.save()
                obj=MyDB.objects.latest('id')
                request.session['id']=obj.id
                return render(request,'home.html',{'userid':request.session['id']})
    else:
        form=MyForm()
    return render(request,'view.html',{'form':form})
def editfun(request,userid):
    obj=MyDB.objects.get(id=userid)
    form=MyForm(request.POST or None,instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            # Setting success flash message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Student data updated successfully'
            )
            # Redirecting user back to student listing
            return render(request,'home.html',{'userid':request.session['id']})
    return render(request,'view.html',{'form':form})
def logoutfunc(request):
    del request.session['id']
    return redirect('myapp:home')