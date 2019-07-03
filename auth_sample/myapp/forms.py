from django import forms
from .models import MyDB
from django.forms import ModelForm

class LoginForm(forms.Form):
    usern=forms.CharField(max_length=50)
    passw=forms.CharField(max_length=50)

class MyForm(ModelForm,forms.Form):
    confirmpassw=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'confirm password'
        }))
    class Meta:

        model=MyDB

        fields=['username','email','passw']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username',
                'required':True
            }),

            'email':forms.TextInput(attrs={

                'class':'form-control',
                'placeholder':'enter email',
                'type':'email',
                'required':True
            }),
            'passw':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter password'
            })
        }
        