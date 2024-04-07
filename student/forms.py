from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Record

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields=['username','password']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address']

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address']