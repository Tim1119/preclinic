from django.urls import path,include
from .views import (PatientProfileView,PatientUpdateProfileView,EmployeeProfileView,EmployeeUpdateProfileView,AllDoctorsView,AllEmployeesView,AllPatientsView)


app_name = 'profiles'

urlpatterns = [
     path('all-patients/', AllPatientsView.as_view(),name='all-patients'),
    path('all-employees/', AllEmployeesView.as_view(),name='all-employees'),
    path('all-doctors/', AllDoctorsView.as_view(),name='all-doctors'),
    path('patient-profile/<str:slug>/', PatientProfileView.as_view(),name='patient-profile'),
    path('patient-update-profile/<str:slug>/', PatientUpdateProfileView.as_view(),name='patient-update-profile'),
    path('employee-profile/<str:slug>/', EmployeeProfileView.as_view(),name='employee-profile'),
    path('employee-update-profile/<str:slug>/', EmployeeUpdateProfileView.as_view(),name='employee-update-profile'),
]
