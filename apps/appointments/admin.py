from django.contrib import admin

# Register your models here.
from .models import Appointment,AdminAppointment,DoctorAppointment

admin.site.register(Appointment)
admin.site.register(AdminAppointment)
admin.site.register(DoctorAppointment)