from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms 

from django.forms import ModelForm
from .models import Sale


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']