from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import  User



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Password again'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name', 'last_name','password1','password2')
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter Username'}),
            'email': forms.EmailInput(attrs={'class':"form-control",'placeholder':'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter Last Name'})
        }
        
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_buyer = True
    #     user.save()
    #     Buyer.objects.create(user=user)
    #     return user
        

      