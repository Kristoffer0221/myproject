from django.contrib import admin
from .models import Task, PatientInformation
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
        'test_date',
        'current_residence_city',
        'current_residence_province',
    )
    list_filter = (
        'sex',
        'civil_status',
        'is_filipino',
        'living_with_partner',
        'currently_pregnant',
        'test_date',
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
    readonly_fields = ('age', 'age_in_months')  # if computed or auto-calculated
    ordering = ('-test_date',)
    fieldsets = (
        ('User Association', {
            'fields': ('user',)
        }),
        ('Testing Details', {
            'fields': ('test_date',)
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