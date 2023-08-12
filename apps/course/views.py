from django.shortcuts import render
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.profiles.custom_permissions import UserIsStaffMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import CourseForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class AllCoursesView(LoginRequiredMixin,UserIsStaffMixin,ListView):
    model = Course
    template_name = 'courses/all_courses.html'
    context_object_name='courses'
    paginate_by = 10

    

class CreateCourseView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,CreateView):
    form_class=CourseForm
    success_message = 'course successfully created'
    success_url = reverse_lazy('courses:all-courses')
    template_name = 'courses/create_course.html'
    context_object_name='course'
    
    

class UpdateCourseView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,UpdateView):
    model=Course
    form_class=CourseForm
    template_name = 'courses/update_course.html'
    success_message = 'course successfully updated'
    success_url = reverse_lazy('courses:all-courses')
    context_object_name='course'
   

class DeleteCourseView(LoginRequiredMixin,UserIsStaffMixin,SuccessMessageMixin,DeleteView):
    model = Course
    success_message = 'course successfully deleted'
    success_url = reverse_lazy('courses:all-courses')
    

    
