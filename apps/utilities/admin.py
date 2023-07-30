from django.contrib import admin
from .models import Institution,EducationInformation,WorkExperience


admin.site.register(Institution)
admin.site.register(EducationInformation)
admin.site.register(WorkExperience)