from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment,DoctorAppointment,AdminAppointment
from apps.profiles.models import Employee,Patient
from django.utils import timezone
# from apps.appointments.models import AdminAppointment
from django.db.models import Sum,Count
from datetime import date
# from .custom_permissions import UserIsEmployeeMixin,UserIsPatientMixin
# LoginRequiredMixin,
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PatientAppointmentForm,DoctorAppointmentForm,AdminAppointmentForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from apps.profiles.custom_permissions import UserIsEmployeeMixin,UserIsPatientMixin,UserIsDoctorMixin,UserIsStaffMixin


#  --------------------------------------------------- Patient Views ---------------------------------------------------------

class PatientHomeView(LoginRequiredMixin,UserIsPatientMixin,TemplateView):
    template_name= 'appointments/patients/index.html'
    context_object_name="appointments"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        total_amount_spent = Appointment.objects.filter(created_by=patient_profile).aggregate(Sum("adminappointment__cost"))['adminappointment__cost__sum']
        pending_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Pending').count()
        approved_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Approved').count()
        completed_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Completed').count()
        
        
        pending_appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Pending')[0:5]
        completed_appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Completed')[0:5]
        approved_appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Approved')[0:5]
        
        context['pending_appointments_count'] = pending_appointments_count
        context['approved_appointments_count'] = approved_appointments_count
        context['completed_appointments_count'] = completed_appointments_count
        context['total_amount_spent'] =total_amount_spent

        context['pending_appointments'] =pending_appointments
        context['completed_appointments'] =completed_appointments
        context['approved_appointments'] =approved_appointments
        return context
    
class AllPatientAppointmentsView(LoginRequiredMixin,UserIsPatientMixin,ListView):
    model = Appointment
    template_name = 'appointments/patients/all_patient_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        appointments = Appointment.objects.filter(created_by=patient_profile)
        return appointments
    
class PendingPatientAppointmentsView(LoginRequiredMixin,UserIsPatientMixin,ListView):
    model = Appointment
    template_name = 'appointments/patients/all_patient_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Pending')
        return appointments
    
class ApprovedPatientAppointmentsView(LoginRequiredMixin,UserIsPatientMixin,ListView):
    model = Appointment
    template_name = 'appointments/patients/all_patient_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Approved')
        return appointments
    
class CompletedPatientAppointmentsView(LoginRequiredMixin,UserIsPatientMixin,ListView):
    model = Appointment
    template_name = 'appointments/patients/all_patient_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        appointments = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Completed')
        return appointments
    
class PatientCreateAppointmentView(LoginRequiredMixin,UserIsPatientMixin,SuccessMessageMixin,CreateView):
    form_class = PatientAppointmentForm
    success_message = 'appointment successfully created'
    success_url = reverse_lazy('appointments:all-patient-appointments')
    template_name = 'appointments/patients/patient_create_appointment.html'
    
    def form_valid(self, form):
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        form.instance.created_by = patient_profile
        return super().form_valid(form)
    

    # def get_form_kwargs(self):
    #     kwargs = super(PatientAppointmentForm, self).get_form_kwargs()
    #     if kwargs['created_by'] is None:
    #         patient_profile = get_object_or_404(Patient,user=self.request.user)
    #     kwargs['instance'].created_by = patient_profile
    #     return kwargs
    
class PatientDetailAppointmentView(LoginRequiredMixin,UserIsPatientMixin,DetailView):
    model = Appointment
    success_url = reverse_lazy('appointments:all-patient-appointments')
    template_name = 'appointments/patients/patient_appointment_detail.html'

    def get_object(self, queryset=None):
        obj = super(PatientDetailAppointmentView, self).get_object()
        if not obj.created_by.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to view an appointment you didn't create")
        return obj
    
class PatientUpdateAppointmentView(LoginRequiredMixin,UserIsPatientMixin,SuccessMessageMixin,UpdateView):
    model=Appointment
    form_class = PatientAppointmentForm
    success_message = 'Appointment successfully updated'
    success_url = reverse_lazy('appointments:all-patient-appointments')
    template_name = 'appointments/patients/patient_update_appointment.html'

    def get_object(self, queryset=None):
        obj = super(PatientUpdateAppointmentView, self).get_object()
        if not obj.created_by.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to update an appointment you didn't create")
        return obj
    
class PatientDeleteAppointmentView(LoginRequiredMixin,UserIsPatientMixin,SuccessMessageMixin,DeleteView):
    model = Appointment
    success_message = 'appointment successfully deleted'
    success_url = reverse_lazy('appointments:all-patient-appointments')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.created_by.user == self.request.user:
            raise PermissionDenied("You don't have permission to delete an appointment you didn't create")
        return obj




#  --------------------------------------------------- Doctor Views ---------------------------------------------------------

class DoctorHomeView(LoginRequiredMixin,UserIsDoctorMixin,TemplateView):
    template_name= 'appointments/employee/index.html'
    context_object_name="appointments"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        doctor_profile = get_object_or_404(Employee,user=self.request.user,role='Doctor')
        pending_appointments_count = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Pending').count()
        upcoming_appointments_count = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Approved').count()
        completed_appointments_count = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Completed').count()
        
        
        pending_appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Pending')[0:5]
        completed_appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Completed')[0:5]
        upcoming_appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Approved')[0:5]
        
        context['pending_appointments_count'] = pending_appointments_count
        context['upcoming_appointments_count'] = upcoming_appointments_count
        context['completed_appointments_count'] = completed_appointments_count
        
        context['pending_appointments'] =pending_appointments
        context['completed_appointments'] =completed_appointments
        context['upcoming_appointments'] =upcoming_appointments
        return context
    
class AllDoctorAppointmentsView(LoginRequiredMixin,UserIsDoctorMixin,ListView):
    model = Appointment
    template_name = 'appointments/employee/all_doctor_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        doctor_profile = get_object_or_404(Employee,user=self.request.user,role='Doctor')
        appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile)
        return appointments
    
class PendingDoctorAppointmentsView(LoginRequiredMixin,UserIsDoctorMixin,ListView):
    model = Appointment
    template_name = 'appointments/employee/all_doctor_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        doctor_profile = get_object_or_404(Employee,user=self.request.user,role='Doctor')
        appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Pending')
        return appointments
    
class UpcomingDoctorAppointmentsView(LoginRequiredMixin,UserIsDoctorMixin,ListView):
    model = Appointment
    template_name = 'appointments/employee/all_doctor_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        doctor_profile = get_object_or_404(Employee,user=self.request.user,role='Doctor')
        appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Approved')
        return appointments
    
class CompletedDoctorAppointmentsView(LoginRequiredMixin,UserIsDoctorMixin,ListView):
    model = Appointment
    template_name = 'appointments/employee/all_doctor_appointment.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        doctor_profile = get_object_or_404(Employee,user=self.request.user)
        appointments = Appointment.objects.filter(adminappointment__employee=doctor_profile,adminappointment__status='Completed')
        return appointments
    
    
class DoctorDetailAppointmentView(LoginRequiredMixin,UserIsDoctorMixin,DetailView):
    model = Appointment
    success_url = reverse_lazy('appointments:all-doctor-appointments')
    template_name = 'appointments/employee/doctor_appointment_detail.html'
    context_object_name='appointment'

    def get_object(self, queryset=None):
        obj = super(DoctorDetailAppointmentView, self).get_object()
        if not obj.adminappointment.employee.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to view an appointment you didn't create")
        return obj
    
class DoctorUpdateAppointmentView(LoginRequiredMixin,UserIsDoctorMixin,SuccessMessageMixin,UpdateView):
    model=DoctorAppointment
    form_class = DoctorAppointmentForm
    success_message = 'Appointment successfully updated'
    success_url = reverse_lazy('appointments:all-doctor-appointments')
    template_name = 'appointments/employee/doctor_update_appointment.html'

    def get_object(self, queryset=None):
        obj = super(DoctorUpdateAppointmentView, self).get_object()
        if not obj.appointment.adminappointment.employee.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to update an appointment you didn't create")
        return obj
    

#  --------------------------------------------------- Admin Views ---------------------------------------------------------

class StaffHomeView(LoginRequiredMixin,UserIsStaffMixin,TemplateView):
    template_name= 'appointments/staff/index.html'
    context_object_name="appointments"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pending_appointments_count = Appointment.objects.filter(adminappointment__status='Pending').count()
        upcoming_appointments_count = Appointment.objects.filter(adminappointment__status='Approved').count()
        completed_appointments_count = Appointment.objects.filter(adminappointment__status='Completed').count()
        
        
        pending_appointments = Appointment.objects.filter(adminappointment__status='Pending')[0:5]
        completed_appointments = Appointment.objects.filter(adminappointment__status='Completed')[0:5]
        upcoming_appointments = Appointment.objects.filter(adminappointment__status='Approved')[0:5]
        
        context['pending_appointments_count'] = pending_appointments_count
        context['upcoming_appointments_count'] = upcoming_appointments_count
        context['completed_appointments_count'] = completed_appointments_count
        
        context['pending_appointments'] =pending_appointments
        context['completed_appointments'] =completed_appointments
        context['upcoming_appointments'] =upcoming_appointments
        return context
    
class AllAppointmentsStaffView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Appointment
    template_name = 'appointments/staff/all_appointments.html'
    context_object_name='appointments'
    paginate_by = 10

    
    
class PendingStaffAppointmentsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Appointment
    template_name = 'appointments/staff/all_appointments.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        appointments = Appointment.objects.filter(adminappointment__status='Pending')
        return appointments
    
class ApprovedStaffAppointmentsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Appointment
    template_name = 'appointments/staff/all_appointments.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        appointments = Appointment.objects.filter(adminappointment__status='Approved')
        return appointments
    
class CompletedStaffAppointmentsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Appointment
    template_name = 'appointments/staff/all_appointments.html'
    context_object_name='appointments'
    paginate_by = 10

    def get_queryset(self):
        appointments = Appointment.objects.filter(adminappointment__status='Completed')
        return appointments
    
    
class StaffDetailAppointmentView(LoginRequiredMixin,UserIsStaffMixin,DetailView):
    model = Appointment
    success_url = reverse_lazy('appointments:all-staff-appointments')
    template_name = 'appointments/staff/staff_appointment_detail.html'
    context_object_name='appointment'

   
class StaffUpdateAppointmentView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,UpdateView):
    model = AdminAppointment
    form_class = AdminAppointmentForm
    success_message = 'Appointment successfully updated'
    success_url = reverse_lazy('appointments:all-staff-appointments')
    template_name = 'appointments/staff/staff_update_appointment.html'

    def get_object(self, queryset=None):
        obj = super(StaffUpdateAppointmentView, self).get_object()
        if not self.request.user.is_staff:
            raise PermissionDenied()
        return obj
    


    