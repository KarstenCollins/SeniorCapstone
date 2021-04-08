from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #user models will be affected
        model = User
        #what fields will be shown on form
        fields = ['username', 'email', 'password1', 'password2']