from django.urls import path,include
from .views import PatientProfileView,PatientUpdateProfileView,EmployeeProfileView,EmployeeUpdateProfileView


app_name = 'accounts'

urlpatterns = [
    path('patient-profile/<str:slug>/', PatientProfileView.as_view(),name='patient-profile-view'),
    path('patient-update-profile/<str:slug>/', PatientUpdateProfileView.as_view(),name='patient-update-profile-view'),
    path('employee-profile/<str:slug>/', EmployeeProfileView.as_view(),name='employee-profile-view'),
    path('employee-update-profile/<str:slug>/', EmployeeUpdateProfileView.as_view(),name='employee-update-profile-view'),
]
