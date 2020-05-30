from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from . models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateTimeField(widget=DateInput(attrs={'type': 'date'}))
    about_me = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'about_me']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    about_me = forms.CharField(max_length=300)
    # date_of_birth = forms.DateTimeField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'about_me']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
