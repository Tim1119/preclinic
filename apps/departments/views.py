from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from .models import HospitalDepartments
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.profiles.custom_permissions import UserIsStaffMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import DepartmentForm

# Create your views here.
class AllDepartmentsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = HospitalDepartments
    template_name = 'departments/all_departments.html'
    context_object_name='departments'
    paginate_by = 10

    

class CreateDepartmentView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,CreateView):
    form_class=DepartmentForm
    success_message = 'department successfully created'
    success_url = reverse_lazy('departments:all-departments')
    template_name = 'departments/create_department.html'
    
    

class UpdateDepartmentView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,UpdateView):
    model= HospitalDepartments
    form_class=DepartmentForm
    template_name = 'departments/update_department.html'
    success_message = 'department successfully updated'
    success_url = reverse_lazy('departments:all-departments')
    context_object_name='department'
   

class DeleteDepartmentView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,DeleteView):
    model = HospitalDepartments
    success_message = 'department successfully deleted'
    success_url = reverse_lazy('departments:all-departments')
    

    
