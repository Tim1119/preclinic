from django.shortcuts import render
from .models import Ailment
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.profiles.custom_permissions import UserIsStaffMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import AilmentForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class AllAilmentsView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Ailment
    template_name = 'ailments/all_ailments.html'
    context_object_name='ailments'
    paginate_by = 10

    

class CreateAilmentsView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,CreateView):
    form_class=AilmentForm
    success_message = 'ailment successfully created'
    success_url = reverse_lazy('ailments:all-ailments')
    template_name = 'ailments/create_ailment.html'
    
    

class UpdateAilmentsView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,UpdateView):
    model=Ailment
    form_class=AilmentForm
    template_name = 'ailments/update_ailment.html'
    success_message = 'ailment successfully updated'
    success_url = reverse_lazy('ailments:all-ailments')
    context_object_name='ailment'
   

class DeleteAilmentsView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,DeleteView):
    model = Ailment
    success_message = 'ailment successfully deleted'
    success_url = reverse_lazy('ailments:all-ailments')
    

    
