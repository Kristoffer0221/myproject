from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, TaskForm, ContactForm1, ContactForm2, PatientInformationForm
from django.contrib.auth.decorators import login_required
from .models import Task, PatientInformation
from formtools.wizard.views import SessionWizardView
from django import forms


class PatientFormStep1(PatientInformationForm):
    class Meta(PatientInformationForm.Meta):
        fields = [
            'test_date',
            'philhealth_number', 'not_enrolled_philhealth',
            'philsys_number', 'no_philsys_number',
            'first_name', 'middle_name', 'last_name', 'suffix',
        ]


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


class PatientInformationWizard(SessionWizardView):
    form_list = [PatientFormStep1, PatientFormStep2, PatientFormStep3]
    template_name = 'patient_info.html'

    def done(self, form_list, **kwargs):
        # Combine all form data into one dictionary
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        patient = PatientInformation(**data)      # 1️⃣ Prepare form data (like form.save(commit=False))
        patient.user = self.request.user          # 2️⃣ Assign logged-in user
        patient.save()                            # 3️⃣ Save to database
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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


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

    return render(request, 'authentication/login.html', {'form': form})

@login_required
def home(request):
    # Get the user's tasks
    task = Task.objects.filter(user=request.user)

    # Try to get the user's patient information (if it exists)
    patient_info = None
    try:
        patient_info = PatientInformation.objects.get(user=request.user)
    except PatientInformation.DoesNotExist:
        patient_info = None

    context = {
        'task': task,
        'patient_info': patient_info,
    }

    return render(request, 'home.html', context)


# Logout View
def logout_view(request):
    if request.method == 'POST':
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

# @login_required
# def add_personal_info(request):
#     if request.method == 'POST':
#         form = PersonalInformationForm(request.POST)
#         if form.is_valid():
#             info = form.save(commit=False)
#             info.user = request.user
#             info.save()
#             return redirect('home')
#     else:
#         form = PersonalInformationForm()
#     return render(request, 'add_personal_info.html', {'form': form})