from django.urls import path
from . import views
from .views import ContactWizard, PatientInformationWizard
from .forms import ContactForm1, ContactForm2
urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add_task/', views.add_task, name = "add_task"),
    # path('personal-info/add/', views.add_personal_info, name='add_personal_info'),
    path('contact/', ContactWizard.as_view([ContactForm1, ContactForm2]), name='contact_wizard'),
    path('patient-info/', PatientInformationWizard.as_view(), name='patient_information_wizard'),
]
