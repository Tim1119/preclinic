from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from .models import Institution
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.profiles.custom_permissions import UserIsStaffMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import InstitutionForm

# Create your views here.
class AllInstitutionsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Institution
    template_name = 'institutions/all_institutions.html'
    context_object_name='institutions'
    paginate_by = 10

    

class CreateInstitutionView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,CreateView):
    model = Institution
    form_class=InstitutionForm
    success_message = 'institution successfully created'
    success_url = reverse_lazy('institutions:all-institutions')
    template_name = 'institutions/create_institution.html'
    context_object_name='institution'
    
    

class UpdateInstitutionView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,UpdateView):
    model = Institution
    form_class=InstitutionForm
    template_name = 'institutions/update_institution.html'
    success_message = 'institution successfully updated'
    success_url = reverse_lazy('institutions:all-institutions')
    context_object_name='institution'
   

class DeleteInstitutionView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,DeleteView):
    model = Institution
    success_message = 'institution successfully deleted'
    success_url = reverse_lazy('institutions:all-institutions')
    

    
