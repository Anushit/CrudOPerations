from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        return cleaned_data