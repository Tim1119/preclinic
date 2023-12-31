from django.db import models
from .utils import BaseProfile
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

    # def save(self, *args, **kwargs):
    #     self.has_updated_profile = True  # Set has_updated_profile to True
    #     super(Patient, self).save(*args, **kwargs)

        
class Employee(BaseProfile):

    class Role(models.TextChoices):
        NURSE = 'Nurse', 'Nurse'
        PHARMACIST = 'Pharmacist', 'Pharmacist'
        LABORATORIST = 'Laboratorist', 'Laboratorist'
        ACCOUNTANT = 'Accountant', 'Accountant'
        RECEPTIONIST = 'Receptionist', 'Receptionist'
        DOCTOR = 'Doctor', 'Doctor'
        
    role = models.CharField(max_length=40,choices=Role.choices)


    def __str__(self):
        return f'Employee account for {self.user.full_name}'
    

    # def save(self, *args, **kwargs):
    #     self.has_updated_profile = True  # Set has_updated_profile to True
    #     super(Employee, self).save(*args, **kwargs)

   

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    




