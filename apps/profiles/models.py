from django.db import models
from .utils import BaseProfile
from apps.utilities.models import EducationInformation,WorkExperience
from django.utils.translation import gettext_lazy as _

class Patient(BaseProfile):

    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'
    
    class BloodType(models.TextChoices):
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'
    
    blood_group = models.CharField(max_length=3, choices=BloodGroup.choices,verbose_name=_("Blood Group"))
    blood_type = models.CharField(max_length=3,choices=BloodType.choices,default=BloodType.O_POSITIVE,)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

        
class Employee(BaseProfile):

    education = models.ForeignKey(EducationInformation,on_delete=models.SET_NULL,null=True)
    work_experience = models.ForeignKey(WorkExperience,on_delete=models.SET_NULL,null=True)
    is_profile_completed = models.BooleanField(default=False)
    is_profile_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"




