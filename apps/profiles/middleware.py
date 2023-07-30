from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.urls import reverse
from .models import Employee,Patient
from django.contrib import  messages



class ProfileUpdateMiddleware:

    def process_request(self, request):
        if request.user.is_authenticated:
            # Check if the user's profile is updated (you can modify this condition based on your logic)
            if request.user.is_patient:
                patient_profile = get_object_or_404(Patient,user=request.user)
                if not patient_profile.has_updated_profile:
                    return redirect(reverse('patient-update-profile', kwargs={'slug':patient_profile.slug }))
                else:
                    return redirect("appointments:patient-home")
                
            elif request.user.is_employee:
                employee_profile = get_object_or_404(Employee,user=request.user)
                if not employee_profile.has_updated_profile:
                    return redirect(reverse('employee-update-profile', kwargs={'slug':employee_profile.slug }))
                elif not employee_profile.is_approved:
                    messages.error(request,"Sorry your profile has not yet been approved by the amin")
                    return redirect("accounts:login")
                else:
                    return redirect("appointments:employee-home")
        else:
           
            return redirect(reverse('login_view'))
