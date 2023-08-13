from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from apps.profiles.models import Employee

class PatientSignupView(SuccessMessageMixin,CreateView):
    form_class = SignUpForm
    template_name = 'accounts/patients/signup.html'
    success_message = "account succesfully created"
    success_url = reverse_lazy('accounts:login')


    def post(self, request):
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.is_employee = False
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/patients/signup.html', {'form': form})


class EmployeeSignupView(SuccessMessageMixin,CreateView):
    form_class = SignUpForm
    template_name = 'accounts/employee/signup.html'
    success_message = "Account succesfully created"
    success_url = reverse_lazy('accounts:login')


    def post(self, request):
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.is_patient = False
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/employee/signup.html', {'form': form})


class LoginAccountView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    authentication_form = SignInForm
    success_message = 'Welcome, you are now logged in'

    # # def form_valid(self, form):
    # #     self.user =form.get_user()
    # #     if self.user.is_authenticated:
    # #         if self.user.is_patient is True:
    # #             return redirect('appointments:all-patient-appointments')  # Replace with your customer dashboard URL
    # #         elif self.user.is_employee is True:
    # #             return redirect("appointments:general-employee-view-for-all-employees")
    # #         elif self.user.is_staff is True:
              
    # #             return redirect('appointments:all-staff-appointments') 
    # #     else:
    # #         print(form.errors)
    # #         messages.info(self.request,message="You do not a permitted account")
    #         redirect("accounts:login")
    def get_success_url(self):
        user = self.request.user

        if user.is_authenticated:
            if user.is_patient:
                return reverse('appointments:all-patient-appointments')
            elif user.is_employee:
                return reverse('appointments:general-employee-view-for-all-employees')
            elif user.is_staff:
                return reverse('appointments:all-staff-appointments')
        messages.info(self.request,"Sorry your account type is not permitted")
        return redirect("accounts:home")


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('accounts:login')  
