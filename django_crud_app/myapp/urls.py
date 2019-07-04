from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'user'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('create/',views.createfunc,name='create'),
    path('login/',views.loginfunc,name='login'),
    path('userhome/',views.userhome,name='userhome'),
    path('deleteuser/<int:user_id>',views.deletefunc,name='deleteuser'),
    path('edituser/<int:user_id>',views.editfunc,name='edituser'),
    path('viewuser/<int:user_id>',views.viewfunc,name='viewuser'),
    path('viewuser/getajax/',views.getajax,name='getajax'),
    path('logoutuser/',views.logoutfunc,name='logoutuser'),

]
