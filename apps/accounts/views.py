from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView,View
from .forms import SignUpForm, RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

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
    authentication_form = RegistrationForm
    success_message = 'Welcome, you are now logged in'

    def get_success_url(self) -> str:
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'email'):
                return redirect("appointments:patient-home")
            if hasattr(user, 'email'):
                return redirect("appointments:employee-home")
        
        return redirect("default:home")


def activate(request):
    return render(request, 'accounts/confirm_activation.html')
