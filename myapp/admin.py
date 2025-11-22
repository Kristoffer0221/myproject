from django.contrib import admin
from .models import Task, PatientInformation, HivTesting
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)

@admin.register(PatientInformation)
class PatientInformationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'sex',
        'age',
        'civil_status',
        'current_residence_city',
        'current_residence_province',
    )
    list_filter = (
        'sex',
        'civil_status',
        'is_filipino',
        'living_with_partner',
        'currently_pregnant',
    )
    search_fields = (
        'first_name',
        'middle_name',
        'last_name',
        'philhealth_number',
        'philsys_number',
        'current_residence_city',
        'current_residence_province',
    )
    readonly_fields = ('age', 'age_in_months')  
    ordering = ('user',)
    fieldsets = (
        ('User Association', {
            'fields': ('user',)
        }),
        ('PhilHealth and PhilSys', {
            'fields': ('philhealth_number', 'not_enrolled_philhealth', 'philsys_number', 'no_philsys_number')
        }),
        ('Personal Information', {
            'fields': (
                'first_name', 'middle_name', 'last_name', 'suffix',
                'mother_first_2_letters', 'father_first_2_letters', 'birth_order',
                'birth_date', 'age', 'age_in_months',
                'sex', 'gender_identity', 'gender_other_specify',
            )
        }),
        ('Address & Birthplace', {
            'fields': (
                'current_residence_city', 'current_residence_province',
                'permanent_residence_city', 'permanent_residence_province',
                'place_of_birth_city', 'place_of_birth_province',
            )
        }),
        ('Nationality', {
            'fields': ('is_filipino', 'other_nationality')
        }),
        ('Civil & Family Information', {
            'fields': (
                'civil_status',
                'living_with_partner',
                'number_of_children',
                'currently_pregnant',
            )
        }),
    )

@admin.register(HivTesting)
class HivTestingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'birth_mother_hiv',
        'sexual_activity_male',
        'sexual_activity_female',
        'tested_before',
        'result',
        'city_municipality',
        'sex_partner_count_male',
        'sex_partner_count_female',
        'condom_use',
    )

    search_fields = (
        'user__username',
        'city_municipality',
        'test_facility',
        'other_reason',
    )

    list_filter = (
        'birth_mother_hiv',
        'sexual_activity_male',
        'sexual_activity_female',
        'tested_before',
        'result',
        'sex_with_male',
        'sex_with_female',
        'condom_use',
    )

    ordering = ('user',)

    readonly_fields = (
        'date_of_last_test',
        'date_paid_for_sex',
        'date_received_payment',
        'date_sex_under_influence',
        'date_shared_needles',
        'date_received_transfusion',
        'date_occupational_exposure',
        'most_recent_anal_or_neovaginal_sex_male',
        'most_recent_anal_or_neovaginal_sex_female',
        'most_recent_condomless_sex_male',
        'most_recent_condomless_sex_female',
    )
