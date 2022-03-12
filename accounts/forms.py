from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserStudent

class CustomUserCreationForm(UserCreationForm):
    class  Meta:
       model = CustomUserStudent
       fields = "__all__"