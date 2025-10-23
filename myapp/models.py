from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class Task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class PatientInformation(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # 1. Test Date
    test_date = models.DateField()

    # 2. PhilHealth and PhilSys
    philhealth_number = models.CharField(max_length=20, blank=True, null=True)
    not_enrolled_philhealth = models.BooleanField(default=False)
    philsys_number = models.CharField(max_length=20, blank=True, null=True)
    no_philsys_number = models.BooleanField(default=False)

    # 3. Name
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=20, blank=True, null=True)

    # 4. Parents' initials and birth order
    mother_first_2_letters = models.CharField(max_length=2)
    father_first_2_letters = models.CharField(max_length=2)
    birth_order = models.PositiveIntegerField()

    # 5. Birth date
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    age_in_months = models.PositiveIntegerField(blank=True, null=True)

    # 6. Sex and Gender
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)

    GENDER_CHOICES = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Other', 'Other'),
    ]
    gender_identity = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    gender_other_specify = models.CharField(max_length=100, blank=True, null=True)

    # 7. Residence information
    current_residence_city = models.CharField(max_length=100)
    current_residence_province = models.CharField(max_length=100)
    permanent_residence_city = models.CharField(max_length=100)
    permanent_residence_province = models.CharField(max_length=100)
    place_of_birth_city = models.CharField(max_length=100)
    place_of_birth_province = models.CharField(max_length=100)

    # 8. Nationality
    is_filipino = models.BooleanField(default=True)
    other_nationality = models.CharField(max_length=100, blank=True, null=True)

    # 9. Civil Status
    CIVIL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    ]
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES)

    # 10. Living with partner
    living_with_partner = models.BooleanField(default=False)
    number_of_children = models.PositiveIntegerField(blank=True, null=True)

    # 11. Pregnancy (for female clients)
    currently_pregnant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"