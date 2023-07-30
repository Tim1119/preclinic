from django.urls import path,include
from .views import PatientSignupView,EmployeeSignupView


app_name = 'accounts'

urlpatterns = [
    path('patient/register/', PatientSignupView.as_view(),name='patient-signup'),
    path('employee/register/', EmployeeSignupView.as_view(),name='employee-signup'),
]
