from django.contrib import admin
from .models import Patient,Employee
from apps.utilities.models import EducationInformation,WorkExperience
admin.site.register(Patient)
# admin.site.register(Employee)

class EducationInformationInline(admin.TabularInline):
    model = EducationInformation
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EducationInformationInline]

admin.site.register(Employee,EmployeeAdmin)