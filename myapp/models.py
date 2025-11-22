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

    # 1. Username, Email, Contact Number, Password
    # username = models.CharField(max_length=150, unique=True)
    # contact_number = models.CharField(max_length=11)
    # email_address = models.EmailField(max_length=254)
    


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
    
     # 12. Contact Information
    contact_number = models.CharField(max_length=11)
    email_address = models.EmailField(max_length=254)
    
    # 13. EDUCATION & OCCUPATION SECTION 
    EDUCATION_CHOICES = [
        ('No grade completed', 'No grade completed'),
        ('Pre-school', 'Pre-school'),
        ('Elementary', 'Elementary'),
        ('Highschool', 'Highschool'),
        ('Vocational', 'Vocational'),
        ('College', 'College'),
        ('Post-Graduate', 'Post-Graduate'),
        ('N/A', 'N/A'),
    ]
    highest_education_attainment = models.CharField(max_length=30, choices=EDUCATION_CHOICES, default='N/A')

    STATUS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    ]

    # 14. School status
    currently_in_school = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N/A')

    # 15. Work status
    currently_working = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N/A')
    current_occupation = models.CharField(max_length=150, blank=True, null=True)
    previous_occupation = models.CharField(max_length=150, blank=True, null=True)

    # 16. Work abroad history
    worked_abroad_past_5_years = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N/A')
    worked_overseas = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N/A')
    year_return_from_abroad = models.PositiveIntegerField(blank=True, null=True)
    work_abroad_location = models.CharField(max_length=150, blank=True, null=True)

    WORK_TYPE_CHOICES = [
        ('Ship', 'On Ship'),
        ('Land', 'On Land'),
        ('N/A', 'N/A'),
    ]
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES, default='N/A')

    last_country_worked = models.CharField(max_length=150, blank=True, null=True)
    last_port_of_exit = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
class HivTesting(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    birth_mother_hiv = models.CharField(
        max_length=20,
        choices=[('Do not know', 'Do not know'), ('No', 'No'), ('Yes', 'Yes')],
        default='Do not know'
    )

    sex_partner_count_male = models.PositiveIntegerField(null=True, blank=True)
    sex_partner_count_female = models.PositiveIntegerField(null=True, blank=True)
    sexual_activity_male = models.BooleanField(default=False)  # Yes/No
    sexual_activity_female = models.BooleanField(default=False)  # Yes/No
    most_recent_anal_or_neovaginal_sex_male = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY
    most_recent_anal_or_neovaginal_sex_female = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY
    most_recent_condomless_sex_male = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY
    most_recent_condomless_sex_female = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY

    # Sex with Male/Female
    sex_with_male = models.BooleanField(default=False)
    sex_with_female = models.BooleanField(default=False)

    # Type of sex acts
    oral = models.BooleanField(default=False)
    anal_inserter = models.BooleanField(default=False)
    anal_receiver = models.BooleanField(default=False)
    vaginal_inserter = models.BooleanField(default=False)
    vaginal_receiver = models.BooleanField(default=False)

    # Condom use
    condom_use = models.CharField(
        max_length=10,
        choices=[('Always', 'Always'), ('Sometimes', 'Sometimes'), ('Never', 'Never')],
        blank=True,
        null=True
    )

    # Risk behavior items
    paid_for_sex = models.BooleanField(default=False)
    date_paid_for_sex = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY

    received_payment_for_sex = models.BooleanField(default=False)
    date_received_payment = models.CharField(max_length=7, blank=True, null=True)

    sex_under_influence = models.BooleanField(default=False)
    date_sex_under_influence = models.CharField(max_length=7, blank=True, null=True)

    shared_needles = models.BooleanField(default=False)
    date_shared_needles = models.CharField(max_length=7, blank=True, null=True)

    received_transfusion = models.BooleanField(default=False)
    date_received_transfusion = models.CharField(max_length=7, blank=True, null=True)

    occupational_exposure = models.BooleanField(default=False)
    date_occupational_exposure = models.CharField(max_length=7, blank=True, null=True)

    # --- REASONS FOR HIV TESTING ---
    possible_exposure = models.BooleanField(default=False)
    recommended_by_physician = models.BooleanField(default=False)
    referred_by_peer_educator = models.BooleanField(default=False)
    employment_overseas = models.BooleanField(default=False)
    employment_local = models.BooleanField(default=False)
    insurance_requirement = models.BooleanField(default=False)
    received_text_invite = models.BooleanField(default=False)
    other_reason = models.CharField(max_length=255, blank=True, null=True)

    # --- PREVIOUS HIV TEST ---
    tested_before = models.BooleanField(default=False)
    date_of_last_test = models.CharField(max_length=7, blank=True, null=True)  # MM/YYYY
    test_facility = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(
        max_length=26,
        choices=[
            ('Reactive', 'Reactive'),
            ('Non-reactive', 'Non-reactive'),
            ('Indeterminate', 'Indeterminate'),
            ('Was not able to get result', 'Was not able to get result')
        ],
        blank=True,
        null=True
    )
    city_municipality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"HIV Test Record #{self.id}"