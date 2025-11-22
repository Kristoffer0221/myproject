from django import forms
from django.contrib.auth.models import User
from .models import Task, PatientInformation, HivTesting

# 🟦 Registration Form
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'name': 'confirm_password',
            'placeholder': 'Confirm password',
            'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
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
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'name': 'email',
                'placeholder': 'Enter email address',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'required': True,
            }),
            'password': forms.PasswordInput(attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Enter password',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
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
            # Step 1: Basic Information
           'first_name', 'middle_name', 'last_name', 'suffix',
            'philhealth_number', 'not_enrolled_philhealth',
            'philsys_number', 'no_philsys_number',
            

            # Step 2: Personal Details
            'mother_first_2_letters', 'father_first_2_letters', 
            'birth_order', 'birth_date', 
            'age', 'age_in_months',
            'sex', 'gender_identity', 'gender_other_specify',

            # Step 3: Location & Status
            'current_residence_city', 'current_residence_province',
            'permanent_residence_city', 'permanent_residence_province',
            'place_of_birth_city', 'place_of_birth_province',
            'is_filipino', 'other_nationality',
            'civil_status', 'living_with_partner',
            'number_of_children', 'currently_pregnant',
            
             # Step 4: Education & Occupation
            'highest_education_attainment', 'currently_in_school',
            'currently_working', 'current_occupation',
            'previous_occupation', 'worked_abroad_past_5_years',
            'worked_overseas', 'year_return_from_abroad',
            'work_abroad_location', 'work_type',
            'last_country_worked', 'last_port_of_exit',
            
        ]
        
        widgets = {
            # Step 1: Basic Information 
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'middle_name': forms.TextInput(attrs={
                'placeholder': 'Middle name (optional)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'suffix': forms.TextInput(attrs={
                'placeholder': 'e.g. Jr., III (optional)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'philhealth_number': forms.TextInput(attrs={
                'id': 'id_philhealth_number',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter PhilHealth Number'
            }),
            'not_enrolled_philhealth': forms.CheckboxInput(attrs={
                'id': 'id_not_enrolled_philhealth',
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'philsys_number': forms.TextInput(attrs={
                'id': 'id_philsys_number',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter PhilSys Number'
            }),
            'no_philsys_number': forms.CheckboxInput(attrs={
                'id': 'id_no_philsys_number',
                'class': 'h-4 w-4 rounded border-gray-300 p-2 text-blue-600 focus:ring-blue-500'
            }),
            'contact_number': forms.TextInput(attrs={
                'placeholder': 'Mobile/Telephone Number',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'email_address': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            
            
            # Step 2: Personal Details - Purple Theme
            'mother_first_2_letters': forms.TextInput(attrs={
                'placeholder': "First 2 letters of mother's name",
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'father_first_2_letters': forms.TextInput(attrs={
                'placeholder': "First 2 letters of father's name",
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'birth_order': forms.NumberInput(attrs={
                'placeholder': 'Birth order (e.g. 1, 2, 3)',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'in years',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'age_in_months': forms.NumberInput(attrs={
                'placeholder': 'in months (if less than 1 year old)',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'sex': forms.Select(attrs={
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'gender_identity': forms.Select(attrs={
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'gender_other_specify': forms.TextInput(attrs={
                'placeholder': 'Specify other gender identity',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),

            # Step 3: Location & Status - Green Theme
            'current_residence_city': forms.TextInput(attrs={
                'placeholder': 'Current city of residence',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'current_residence_province': forms.TextInput(attrs={
                'placeholder': 'Current province',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'permanent_residence_city': forms.TextInput(attrs={
                'placeholder': 'Permanent city of residence',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'permanent_residence_province': forms.TextInput(attrs={
                'placeholder': 'Permanent province',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'place_of_birth_city': forms.TextInput(attrs={
                'placeholder': 'City of birth',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'place_of_birth_province': forms.TextInput(attrs={
                'placeholder': 'Province of birth',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'is_filipino': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'civil_status': forms.Select(attrs={
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'living_with_partner': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'currently_pregnant': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'other_nationality': forms.TextInput(attrs={
                'placeholder': 'Specify other nationality',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),
            'number_of_children': forms.NumberInput(attrs={
                'placeholder': 'Number of children (if any)',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),

            # ✅ Step 4: Education & Occupation Section - Blue Theme
            'highest_education_attainment': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'currently_in_school': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'currently_working': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'current_occupation': forms.TextInput(attrs={
                'placeholder': 'Enter your current occupation (if any)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'previous_occupation': forms.TextInput(attrs={
                'placeholder': 'Previous occupation in the past 12 months (if any)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'worked_abroad_past_5_years': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'worked_overseas': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'year_return_from_abroad': forms.NumberInput(attrs={
                'placeholder': 'Year returned from last contract (e.g., 2023)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'work_abroad_location': forms.TextInput(attrs={
                'placeholder': 'Where were you based abroad?',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'work_type': forms.Select(attrs={
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'last_country_worked': forms.TextInput(attrs={
                'placeholder': 'Country last worked in',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'last_port_of_exit': forms.TextInput(attrs={
                'placeholder': 'Last port of exit (for seafarers)',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            
        }
    
    
YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No'),
]

    
class HivTestingForm(forms.ModelForm):
    class Meta:
        model = HivTesting
        fields = [
            # STEP 1: HISTORY OF EXPOSURE / RISK ASSESSMENT
            'birth_mother_hiv', 'sex_partner_count_male', 'sex_partner_count_female', 'sexual_activity_male', 'sexual_activity_female',
            'most_recent_anal_or_neovaginal_sex_male', 'most_recent_anal_or_neovaginal_sex_female', 'most_recent_condomless_sex_male', 'most_recent_condomless_sex_female',
            'sex_with_male', 'sex_with_female',
            'oral', 'anal_inserter', 'anal_receiver', 'vaginal_inserter', 'vaginal_receiver',
            'condom_use',
            'paid_for_sex', 'date_paid_for_sex',
            'received_payment_for_sex', 'date_received_payment',
            'sex_under_influence', 'date_sex_under_influence',
            'shared_needles', 'date_shared_needles',
            'received_transfusion', 'date_received_transfusion',
            'occupational_exposure', 'date_occupational_exposure',

            # STEP 2: REASONS FOR HIV TESTING
            'possible_exposure', 'recommended_by_physician', 'referred_by_peer_educator',
            'employment_overseas', 'employment_local', 'insurance_requirement',
            'received_text_invite', 'other_reason',

            # STEP 3: PREVIOUS HIV TEST
            'tested_before', 'date_of_last_test', 'test_facility',
            'result', 'city_municipality',
        ]
        
        labels = {
            'birth_mother_hiv': 'Did your birth mother have HIV when you were born?', 
        }

        widgets = {
            # STEP 1: HISTORY OF EXPOSURE / RISK ASSESSMENT - BLUE THEME
             'birth_mother_hiv': forms.Select(attrs={
                'required': True,
                'class': 'rounded-lg p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ',
                
            }),
            'sex_partner_count_male': forms.NumberInput(attrs={
                'placeholder': 'Number of male sex partners',
                'required': True,
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            }),

            'sex_partner_count_female': forms.NumberInput(attrs={
                'placeholder': 'Number of female sex partners',
                'required': True,
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            }),

            'sexual_activity_male': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'sexual_activity_female': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'most_recent_anal_or_neovaginal_sex_male': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'most_recent_anal_or_neovaginal_sex_female': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'most_recent_condomless_sex_male': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'most_recent_condomless_sex_female': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),

            # TYPE OF SEXUAL PARTNER / ACTS
            'sex_with_male': forms.RadioSelect(choices=YES_NO_CHOICES),
            'sex_with_female': forms.RadioSelect(choices=YES_NO_CHOICES),
            'oral': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'anal_inserter': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'anal_receiver': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'vaginal_inserter': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            'vaginal_receiver': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
            
            # CONDOM USE
            'condom_use': forms.Select(attrs={
                'required': True,
                'class': '  rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ',
            }),

            # RISK BEHAVIORS
            'paid_for_sex': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_paid_for_sex': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'received_payment_for_sex': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_received_payment': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'sex_under_influence': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_sex_under_influence': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'shared_needles': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_shared_needles': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'received_transfusion': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_received_transfusion': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'occupational_exposure': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={     
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_occupational_exposure': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),

            # STEP 2: REASONS FOR HIV TESTING - PURPLE THEME
            'possible_exposure': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'recommended_by_physician': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'referred_by_peer_educator': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'employment_overseas': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'employment_local': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'insurance_requirement': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'received_text_invite': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500'
            }),
            'other_reason': forms.TextInput(attrs={
                'placeholder': 'Please specify other reason (if any)',
                'class': 'w-full rounded-lg border-purple-300 p-2 shadow-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500'
            }),

            # STEP 3: PREVIOUS HIV TEST - GREEN THEME
            'tested_before': forms.RadioSelect(
                choices=YES_NO_CHOICES,
                attrs={     
                    'class': 'flex space-x-6 ',  # horizontal spacing
                }
            ),
            'date_of_last_test': forms.TextInput(attrs={
                'placeholder': 'MM/YYYY',
                'class': 'rounded-lg border-green-300 p-2 shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500'
            }),
            'test_facility': forms.TextInput(attrs={
                'placeholder': 'Enter HTS provider',
                'class': 'rounded-lg border-green-300 p-2 shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500'
            }),
            'result': forms.Select(attrs={
                'class': 'w-full rounded-lg border-green-300 p-2 shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500'
            }),
            'city_municipality': forms.TextInput(attrs={
                'placeholder': 'Enter city or municipality',
                'class': 'rounded-lg border-green-300 p-2 shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500'
            }),
        }

        
class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)