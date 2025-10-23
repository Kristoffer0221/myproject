from django import forms
from django.contrib.auth.models import User
from .models import Task, PatientInformation

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
        
class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        fields = [
            'user',
            'test_date',

            'philhealth_number',
            'not_enrolled_philhealth',
            'philsys_number',
            'no_philsys_number',

            'first_name',
            'middle_name',
            'last_name',
            'suffix',

            'mother_first_2_letters',
            'father_first_2_letters',
            'birth_order',

            'birth_date',
            'age',
            'age_in_months',

            'sex',
            'gender_identity',
            'gender_other_specify',

            'current_residence_city',
            'current_residence_province',
            'permanent_residence_city',
            'permanent_residence_province',
            'place_of_birth_city',
            'place_of_birth_province',

            'is_filipino',
            'other_nationality',

            'civil_status',
            'living_with_partner',
            'number_of_children',

            'currently_pregnant',
        ]

        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'philhealth_number': forms.TextInput(attrs={'class': 'form-control'}),
            'philsys_number': forms.TextInput(attrs={'class': 'form-control'}),

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control'}),

            'mother_first_2_letters': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'father_first_2_letters': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'birth_order': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),

            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'age_in_months': forms.NumberInput(attrs={'class': 'form-control'}),

            'sex': forms.Select(attrs={'class': 'form-select'}),
            'gender_identity': forms.Select(attrs={'class': 'form-select'}),
            'gender_other_specify': forms.TextInput(attrs={'class': 'form-control'}),

            'current_residence_city': forms.TextInput(attrs={'class': 'form-control'}),
            'current_residence_province': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_residence_city': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_residence_province': forms.TextInput(attrs={'class': 'form-control'}),
            'place_of_birth_city': forms.TextInput(attrs={'class': 'form-control'}),
            'place_of_birth_province': forms.TextInput(attrs={'class': 'form-control'}),

            'other_nationality': forms.TextInput(attrs={'class': 'form-control'}),

            'civil_status': forms.Select(attrs={'class': 'form-select'}),
            'number_of_children': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
        
class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)