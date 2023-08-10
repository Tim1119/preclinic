from django.contrib import admin
from .models import Institution,EducationInformation,WorkExperience,Course,HospitalDepartments,Ailment


admin.site.register(Institution)
admin.site.register(EducationInformation)
admin.site.register(WorkExperience)
admin.site.register(Course)
admin.site.register(HospitalDepartments)
admin.site.register(Ailment)