from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,UpdateView,ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .custom_permissions import UserIsEmployeeMixin,UserIsStaffMixin,UserIsPatientMixin,UserIsDoctorMixin
from .models import Employee,Patient
from .forms import PatientProfileForm,EmployeeProfileForm
from apps.appointments.models import Appointment,AdminAppointment,Employee
from django.db.models import Sum,Count
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class PatientProfileView(SuccessMessageMixin,UserIsPatientMixin,LoginRequiredMixin,DetailView):
    model = Patient
    context_object_name='profile'
    template_name = 'profiles/patients/patient_profile.html'
    

    def get_object(self, queryset=None):
        patient_profile = super(PatientProfileView, self).get_object()
        if patient_profile.user != self.request.user:
            raise PermissionDenied("You do not permission to view a profile that's not yours")
        return patient_profile
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        patient_profile = get_object_or_404(Patient,user=self.request.user)
        total_amount_spent = Appointment.objects.filter(created_by=patient_profile).aggregate(Sum("adminappointment__cost"))['adminappointment__cost__sum']
        pending_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Pending').count()
        approved_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Approved').count()
        completed_appointments_count = Appointment.objects.filter(created_by=patient_profile,adminappointment__status='Completed').count()

        context['pending_appointments_count'] = pending_appointments_count
        context['approved_appointments_count'] = approved_appointments_count
        context['completed_appointments_count'] = completed_appointments_count
        context['total_amount_spent'] =total_amount_spent

        return context
    

class PatientUpdateProfileView(SuccessMessageMixin,UserIsPatientMixin,LoginRequiredMixin,UpdateView):
    model= Patient
    form_class = PatientProfileForm
    success_message = 'Your profile successfully updated'
    template_name = 'profiles/patients/patient_update_profile.html'
    context_object_name='profile'

    def get_object(self, queryset=None):
        patient_profile = super().get_object(queryset)
        if patient_profile.user != self.request.user:
            raise PermissionDenied("You do not permission to update a profile that's not yours")
        return patient_profile
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user.patient.has_updated_profile = True
        self.object.user.patient.save()
        return response
    
    def get_success_url(self):
        return reverse('profiles:patient-profile', kwargs={'slug': self.object.slug})
    

class EmployeeProfileView(UserIsEmployeeMixin,LoginRequiredMixin,DetailView):
    model = Employee
    template_name = 'profiles/employee/employee_profile.html'
    context_object_name='profile'

    def get_object(self, queryset=None):
        employee = super(EmployeeProfileView,self).get_object()
        # if (employee.user != self.request.user) or (self.request.user.is_staff is False):
        if (employee.user != self.request.user):
            raise PermissionDenied("You do not permission to view a profile that's not yours")
        return employee
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        employee_profile = get_object_or_404(Employee,user=self.request.user)
        if employee_profile.role == 'Doctor':
            total_amount_spent = Appointment.objects.filter(adminappointment__employee=employee_profile).aggregate(Sum("adminappointment__cost"))['adminappointment__cost__sum']
            pending_appointments_count = Appointment.objects.filter(adminappointment__employee=employee_profile,adminappointment__status='Pending').count()
            upcoming_appointments_count = Appointment.objects.filter(adminappointment__employee=employee_profile,adminappointment__status='upcoming').count()
            completed_appointments_count = Appointment.objects.filter(adminappointment__employee=employee_profile,adminappointment__status='Completed').count()

            context['pending_appointments_count'] = pending_appointments_count
            context['upcoming_appointments_count'] = upcoming_appointments_count
            context['completed_appointments_count'] = completed_appointments_count
            context['total_amount_spent'] =total_amount_spent

        return context


class EmployeeUpdateProfileView(UserIsEmployeeMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= Employee
    form_class = EmployeeProfileForm
    success_message = 'Employee profile successfully updated'
    context_object_name='profile'
    template_name = 'profiles/employee/employee_update_profile.html'

    def get_object(self, queryset=None):
        employee = super().get_object()
        if employee.user != self.request.user:
            raise PermissionDenied("You do not permission to update a profile that's not yours")
        return employee
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user.employee.has_updated_profile = True
        self.object.user.employee.save()
        return response

    def get_success_url(self):
        return reverse('profiles:employee-profile', kwargs={'slug': self.object.slug})
    

class AllPatientsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model=Patient
    context_object_name='profiles'
    template_name = 'profiles/staff/all_profiles.html'
    paginate_by = 10

class AllEmployeesView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model=Employee
    context_object_name='profiles'
    template_name = 'profiles/staff/all_profiles.html'
    paginate_by = 10

class AllDoctorsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model=Employee
    context_object_name='doctors'
    template_name = 'profiles/staff/all_doctors.html'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Employee.objects.filter(role='Doctor')