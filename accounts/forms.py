from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoleForm(forms.Form):
    ROLE_CHOICES = [
        ('teacher', 'Вчитель'),
        ('student', 'Студент'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
