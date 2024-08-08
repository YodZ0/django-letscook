from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=70)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=70)
    email = forms.CharField(widget=forms.EmailInput(), help_text='example: username@email.com')
    password1 = forms.CharField(min_length=8,
                                widget=forms.PasswordInput(),
                                help_text='password should have at least 8 simbols')
    password2 = forms.CharField(min_length=8,
                                widget=forms.PasswordInput(),
                                help_text='please write password again')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
