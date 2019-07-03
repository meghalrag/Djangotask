from django.contrib import admin
from django.urls import path,include
from . import views
app_name='myapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homefunc,name='home'),
    path('reguser/',views.myfunc,name='reguser'),
    path('edituser/<int:userid>',views.editfun,name='edituser'),
    path('logoutuser/',views.logoutfunc,name='logoutuser')
]
