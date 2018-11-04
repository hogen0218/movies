from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
