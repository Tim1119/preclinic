from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView,UpdateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .custom_permissions import UserIsEmployeeMixin,UserIsPatientMixin


class PatientProfileView(UserIsPatientMixin,LoginRequiredMixin,DetailView):

    def get_object(self, queryset):
        patient_profile = super().get_object(queryset)
        if patient_profile.user != self.request.user:
            raise PermissionDenied
        return patient_profile

class PatientUpdateProfileView(UserIsPatientMixin,LoginRequiredMixin,UpdateView):

    def get_object(self, queryset):
        patient_profile = super().get_object(queryset)
        if patient_profile.user != self.request.user:
            raise PermissionDenied
        return patient_profile


class EmployeeProfileView(UserIsEmployeeMixin,LoginRequiredMixin,DetailView):

    def get_object(self, queryset):
        employee_profile = super().get_object(queryset)
        if employee_profile.user != self.request.user:
            raise PermissionDenied
        return employee_profile

class EmployeeUpdateProfileView(UserIsEmployeeMixin,LoginRequiredMixin,UpdateView):

    def get_object(self, queryset):
        employee_profile = super().get_object(queryset)
        if employee_profile.user != self.request.user:
            raise PermissionDenied
        return employee_profile
