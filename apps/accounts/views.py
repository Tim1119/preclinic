from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from apps.profiles.models import Employee,Patient

class PatientSignupView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'accounts/patients/signup.html'
    success_message = "Account succesfully created"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_patient = True
        user.is_employee = False
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your form.")
        return super().form_invalid(form)


class EmployeeSignupView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'accounts/employee/signup.html'
    success_message = "Account successfully created"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_employee = True
        user.is_patient = False
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your form.")
        return super().form_invalid(form)

class LoginAccountView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    authentication_form = SignInForm
    success_message = 'Welcome, you are now logged in'

    def get(self, request, *args, **kwargs):
        print('----->')
        messages_list = messages.get_messages(request)
        for message in messages_list:
            print(message)
        return super().get(request, *args, **kwargs)

  
    def get_success_url(self):
        user = self.request.user

        if user.is_authenticated:
            if user.is_patient:
                if self.request.user.patient.has_updated_profile:
                    return reverse('appointments:all-patient-appointments')
                else:
                    return reverse('profiles:patient-update-profile', kwargs={'slug':user.patient.slug})
            if self.request.user.is_employee:
                if self.request.user.employee.has_updated_profile:
                    return reverse('appointments:general-employee-view-for-all-employees')
                else:
                    return reverse('profiles:employee-update-profile', kwargs={'slug': user.employee.slug})
            elif user.is_staff:
                return reverse('appointments:all-staff-appointments')
            else:
                messages.info(self.request,"Sorry your account type is not permitted")
                return reverse("accounts:login")


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('accounts:login')  
