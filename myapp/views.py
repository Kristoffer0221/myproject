from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, TaskForm, ContactForm1, ContactForm2, PatientInformationForm, HivTestingForm
from django.contrib.auth.decorators import login_required
from .models import Task, PatientInformation, HivTesting, User
from formtools.wizard.views import SessionWizardView
from django import forms
from django.http import FileResponse
from .pdf_generator import generate_patient_pdf

def dashboard(request):
    return render(request, "dashboard.html")

def download_patient_pdf(request, pk):
    patient = PatientInformation.objects.get(pk=pk)
    try:
        hiv_testing = HivTesting.objects.get(user=patient.user)
    except HivTesting.DoesNotExist:
        hiv_testing = None 

    # Generate PDF
    pdf_path = generate_patient_pdf(patient, hiv_testing)
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename=f"{patient.last_name}_{patient.first_name}_form.pdf")

class PatientFormStep1(PatientInformationForm):
    
     # Add Registration fields
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username',
            'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'w-full rounded-lg border-blue-300 p-2 shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    
    class Meta(PatientInformationForm.Meta):
        fields = [
            'username', 'email', 'password', 'confirm_password',
            'first_name', 'middle_name', 'last_name', 'suffix',
            'contact_number', 
            'philhealth_number', 'not_enrolled_philhealth',
            'philsys_number', 'no_philsys_number',        
        ]
    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get("password")
        cpwd = cleaned.get("confirm_password")

        if pwd and cpwd and pwd != cpwd:
            self.add_error("confirm_password", "Password does not match.")

        return cleaned

class PatientFormStep2(PatientInformationForm):
    class Meta(PatientInformationForm.Meta):
        fields = [
            'mother_first_2_letters', 'father_first_2_letters', 'birth_order',
            'birth_date', 'age', 'age_in_months',
            'sex', 'gender_identity', 'gender_other_specify',
            'current_residence_city', 'current_residence_province',
            'permanent_residence_city', 'permanent_residence_province',
            'place_of_birth_city', 'place_of_birth_province',
        ]

class PatientFormStep3(PatientInformationForm):
    class Meta(PatientInformationForm.Meta):
        fields = [
            'is_filipino', 'other_nationality',
            'civil_status', 'living_with_partner',
            'number_of_children', 'currently_pregnant',
        ]
        
class PatientFormStep4(PatientInformationForm):
    class Meta(PatientInformationForm.Meta):
        fields = [
            'highest_education_attainment', 'currently_in_school', 
            'currently_working', 'current_occupation', 
            'previous_occupation', 'worked_abroad_past_5_years',
            'worked_overseas', 'year_return_from_abroad',
            'work_abroad_location', 'work_type',
            'last_country_worked', 'last_port_of_exit',
        ]

class PatientInformationWizard(SessionWizardView):
    form_list = [PatientFormStep1, PatientFormStep2, PatientFormStep3, PatientFormStep4]
    template_name = 'patient_info.html'

    def done(self, form_list, **kwargs):

        # -----------------------------
        # 1️⃣ Extract cleaned data
        # -----------------------------
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        # -----------------------------
        # 2️⃣ Create USER account
        # -----------------------------
        username = data.pop('username')
        email = data.pop('email')
        password = data.pop('password')
        data.pop('confirm_password')   # Remove confirm field

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # -----------------------------
        # 3️⃣ Create PATIENT INFORMATION
        # -----------------------------
        patient = PatientInformation(**data)
        patient.user = user
        patient.save()

        return redirect('login')
 
class HivTestingFormStep1(HivTestingForm):
    class Meta(HivTestingForm.Meta):
        fields = [
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
        ]

class HivTestingFormStep2(HivTestingForm):
    class Meta(HivTestingForm.Meta):
        fields = [
            'possible_exposure', 'recommended_by_physician', 'referred_by_peer_educator',
            'employment_overseas', 'employment_local', 'insurance_requirement',
            'received_text_invite', 'other_reason',
        ]

class HivTestingFormStep3(HivTestingForm):
    class Meta(HivTestingForm.Meta):
        fields = [
            'tested_before', 'date_of_last_test', 'test_facility',
            'result', 'city_municipality',
        ]

class HivTestingWizard(SessionWizardView):
    form_list = [HivTestingFormStep1, HivTestingFormStep2, HivTestingFormStep3]
    template_name = 'hivtesting_form.html'

    def done(self, form_list, **kwargs):
        hiv_testing = form_list[0].save(commit=False)
        hiv_testing.user = self.request.user
        hiv_testing.save()
        return redirect('home')

class ContactWizard(SessionWizardView):
    form_list = [ContactForm1, ContactForm2]
    template_name = 'contact_form.html'

    def done(self, form_list, **kwargs):
        # Process the completed forms
        return render(self.request, 'home.html', {'form_data': [form.cleaned_data for form in form_list]})

# Register View
def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        patient_form = PatientInformationForm(request.POST)

        if reg_form.is_valid() and patient_form.is_valid():

            # ----- CREATE USER -----
            user = reg_form.save(commit=False)
            user.set_password(reg_form.cleaned_data['password'])
            user.save()

            # ----- CREATE PATIENT INFORMATION -----
            patient = patient_form.save(commit=False)
            patient.user = user  
            patient.save()

            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')

    else:
        reg_form = RegistrationForm()
        patient_form = PatientInformationForm()

    return render(
        request,
        'authentication/register.html',
        {
            'form': reg_form,
            'patient_form': patient_form,
        }
    )


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_superuser:
                    messages.success(request, f'Welcome Admin {user.username}!')
                    return redirect('/admin')
                else:
                    return redirect('home')  
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    # Get the user's tasks
    task = Task.objects.filter(user=request.user)

    # Try to get the user's patient information (if it exists)
    # Get user's patient info (if exists)
    patient_info = PatientInformation.objects.filter(user=request.user).first()
    hiv_testings = HivTesting.objects.filter(user=request.user).first()

    context = {
        'task': task,
        'patient_info': patient_info,
        'hiv_testings': hiv_testings,
    }

    return render(request, 'home.html', context)


# Logout View
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    
@login_required
def add_task(request):
    if request.method == 'POST': #IF method is POST
        form = TaskForm(request.POST) #Get form
        if form.is_valid(): #If the form is valid
            task = form.save(commit=False)# Do not save to database immediately
            task.user = request.user # Because you want to get the assigned user first
            form.save()#then save the form
            return redirect('home')
    
    else:
        form = TaskForm()
        
        return render (request, "add_task.html", {'form':form})

