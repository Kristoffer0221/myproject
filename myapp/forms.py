from django import forms
from django.contrib.auth.models import User
from .models import Task

# 🟦 Registration Form
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'name': 'confirm_password',
            'placeholder': 'Confirm password',
            'class': 'form-input',
            'required': True,
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'name': 'username',
                'placeholder': 'Enter username',
                'class': 'form-input',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'name': 'email',
                'placeholder': 'Enter email address',
                'class': 'form-input',
                'required': True,
            }),
            'password': forms.PasswordInput(attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Enter password',
                'class': 'form-input',
                'required': True,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


# 🟩 Login Form
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username',
            'class': 'form-input',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-input',
            'required': True,
        })
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Task Title',
                'class': 'form-input',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Task Description',
                'class': 'form-textarea',
                'required': True,
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }