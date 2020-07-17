from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(max_length=128, label="Username", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(max_length=128, label="Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    captcha = CaptchaField(label='Captcha')

class RegisterForm(forms.Form):
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to tell')
    )
    username = forms.CharField(max_length=128, label="Username", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(max_length=128, label="Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    password_confirm = forms.CharField(max_length=128, label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label='Gender', choices=gender)
    captcha = CaptchaField(label='Captcha')