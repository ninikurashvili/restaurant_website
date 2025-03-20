from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15,required=True)
    location = forms.CharField(max_length=255,required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'location', 'password1', 'password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'location']