from django.urls import path,include
from .views import PatientProfileView,PatientUpdateProfileView,EmployeeProfileView,EmployeeUpdateProfileView


app_name = 'profiles'

urlpatterns = [
    path('patient-profile/<str:slug>/', PatientProfileView.as_view(),name='patient-profile'),
    path('patient-update-profile/<str:slug>/', PatientUpdateProfileView.as_view(),name='patient-update-profile'),
    path('employee-profile/<str:slug>/', EmployeeProfileView.as_view(),name='employee-profile'),
    path('employee-update-profile/<str:slug>/', EmployeeUpdateProfileView.as_view(),name='employee-update-profile'),
]
