from django.db import models
from apps.utilities.models import  TimeStampedUUIDModel
from apps.ailment.models import Ailment
from apps.profiles.models import Employee,Patient
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
import secrets
from apps.departments.models import HospitalDepartments


User = get_user_model()

class Appointment(TimeStampedUUIDModel):
    ref = models.CharField(max_length=200,null=True,blank=True,unique=True)
    created_by = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name=_("created by"))
    title = models.CharField(verbose_name=_("Summarise how you're feeling / ailment"),max_length=300)
    appointment_date = models.DateField(verbose_name=_("Appointment date"),help_text='YYYY-MM-DD')
    slug = AutoSlugField(populate_from='title', unique=True)
    department = models.ForeignKey(HospitalDepartments,null=True,blank=True,on_delete=models.SET_NULL) 
    description = models.TextField(verbose_name=_("Describe how you're feeling"))
  
    def __str__(self) -> str:
        return f"Appointment created for {self.title}"
    
    class Meta:
        ordering = ['-created_at']
    
class AdminAppointment(TimeStampedUUIDModel):

    class AppointmentStatus(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        APPROVED = 'Approved', 'Approved'
        COMPLETED = 'Completed', 'Completed'

    start_time =models.TimeField(null=True,blank=True)
    end_time =models.TimeField(null=True,blank=True)
    slug = AutoSlugField(populate_from='id', unique=True)
    cost = models.IntegerField(default=0,validators=[MinValueValidator(limit_value=0,message='Minimum value of cost is 0')])
    status = models.CharField(max_length=260,choices=AppointmentStatus.choices,default=AppointmentStatus.PENDING)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    appointment = models.OneToOneField(Appointment,null=True,on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"Admin Appointment created for {self.appointment.title}"

class DoctorAppointment(TimeStampedUUIDModel):
    ailment = models.ForeignKey(Ailment,null=True,on_delete=models.SET_NULL,blank=True)
    appointment = models.OneToOneField(Appointment,null=True,on_delete=models.CASCADE)
    symptoms =models.TextField()
    recommendation = models.TextField()
    drugs = models.TextField()
    slug = AutoSlugField(populate_from='appointment', unique=True)

    def __str__(self) -> str:
        return f"Doctor Appointment created for {self.appointment.title}"
   