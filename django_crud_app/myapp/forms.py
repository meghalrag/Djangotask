from django import forms
from phone_field import PhoneField
from .models import LoginDB,UserDB
from django.forms import ModelForm
GENDER = [('1', 'Male'), ('2', 'Female')]
QUAL_TYPE= [('sslc','SSLC'),('plustwo','PLUSTWO'),('degree','DEGREE'),('pg','PG')]
DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015')
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,required=True,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(max_length=50,required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
class RegForm(forms.Form):

#to design model form we use this syntax $ModelForm
#    ''' widgets = {1111
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'name':'name',
#                 'placeholder': 'Enter Name',
#                 'required':True,
#             }),
#             'email':forms.EmailInput(attrs={
#                 'class':'form-control',
#                 'placeholder':'Enter emailid',
#                 'required':True,
#             }),
#     }'''
    usernamereg=forms.CharField(max_length=50,required=True,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    passwordreg=forms.CharField(min_length=8,required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    cpasswordreg=forms.CharField(min_length=8,required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password again'}))
    name = forms.CharField(max_length = 100,required = True,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'enter name',
            'pattern' : "[A-Za-z]+"
            }))
    email = forms.CharField(required= True,
    widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder':'enter email'
            }))
    phone = PhoneField(blank=True, help_text='Contact phone number')
    Mobile_Number=forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'mobile number',
                'minlength':"10",
                'maxlength':"10"
            }))
    Gender=forms.CharField(widget=forms.RadioSelect(attrs={'required':True},
                choices=GENDER
            ))

    city=forms.CharField(max_length=100,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'enter city',
            'required':True,
            'pattern':"[a-zA-Z]+"

    }))
    qualification=forms.ChoiceField(
        widget=forms.Select(
            attrs={'class':'form-control'}),
            choices=QUAL_TYPE)
    dob=forms.DateField(widget=forms.SelectDateWidget(attrs={'class':''},years=DOY))