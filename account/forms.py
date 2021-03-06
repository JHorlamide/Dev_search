from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile, Skill


class RegisterForm(UserCreationForm):
    email = forms.CharField(
        max_length=255, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'Full Name'
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'id': 'formInput#text'})


class LoginForm(UserCreationForm):
    email = forms.CharField(
        max_length=255, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('email', 'password')


class AccountForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'id': 'formInput#text'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'id': 'formInput#text'})
