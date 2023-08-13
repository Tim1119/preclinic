from django.urls import path,include
from .views import (PatientHomeView,PatientCreateAppointmentView,PatientDeleteAppointmentView,
                    PatientUpdateAppointmentView,PatientDetailAppointmentView,AllPatientAppointmentsView,
                    PendingPatientAppointmentsView,ApprovedPatientAppointmentsView,CompletedPatientAppointmentsView,
                    DoctorHomeView,AllDoctorAppointmentsView,PendingDoctorAppointmentsView,UpcomingDoctorAppointmentsView,
                    CompletedDoctorAppointmentsView,DoctorDetailAppointmentView,DoctorUpdateAppointmentView,
                    StaffHomeView,AllAppointmentsStaffView,PendingStaffAppointmentsView,CompletedStaffAppointmentsView,ApprovedStaffAppointmentsView,
                    StaffDetailAppointmentView,StaffUpdateAppointmentView,GeneralEmployeeViewForNonDoctors
                    )


app_name = 'appointments'

admin_patterns = [
    path('staff-home/', StaffHomeView.as_view(),name='staff-home-view'),
    path('all-appointments/', AllAppointmentsStaffView.as_view(),name='all-staff-appointments'),
    path('pending-staff-appointments/', PendingStaffAppointmentsView.as_view(),name='pending-staff-appointments'),
    path('approved-staff-appointments/', ApprovedStaffAppointmentsView.as_view(),name='approved-staff-appointments'),
    path('completed-staff-appointments/', CompletedStaffAppointmentsView.as_view(),name='completed-staff-appointments'),
    path('get-staff-appointment/<str:slug>/', StaffDetailAppointmentView.as_view(),name='staff-appointment-detail'),
    path('update-staff-appointment/<str:slug>/', StaffUpdateAppointmentView.as_view(),name='update-staff-appointment'),
    # path('delete-staff-appointment/<str:slug>/', StaffDeleteAppointmentView.as_view(),name='delete-staff-appointment'),
]

patient_patterns = [
    path('doctor-home/', PatientHomeView.as_view(),name='patient-home-view'),
    path('all-patient-appointments/', AllPatientAppointmentsView.as_view(),name='all-patient-appointments'),
    path('pending-patient-appointments/', PendingPatientAppointmentsView.as_view(),name='pending-patient-appointments'),
    path('approved-patient-appointments/', ApprovedPatientAppointmentsView.as_view(),name='approved-patient-appointments'),
    path('completed-patient-appointments/', CompletedPatientAppointmentsView.as_view(),name='completed-patient-appointments'),
    path('create-patient-appointment/', PatientCreateAppointmentView.as_view(),name='create-patient-appointment'),
    path('get-patient-appointment/<str:slug>/', PatientDetailAppointmentView.as_view(),name='patient-appointment-detail'),
    path('update-patient-appointment/<str:slug>/', PatientUpdateAppointmentView.as_view(),name='update-patient-appointment'),
    path('delete-patient-appointment/<str:slug>/', PatientDeleteAppointmentView.as_view(),name='delete-patient-appointment'),
]
doctor_patterns = [
    path('patient-home/', DoctorHomeView.as_view(),name='doctor-home-view'),
    path('all-doctor-appointments/', AllDoctorAppointmentsView.as_view(),name='all-doctor-appointments'),
    path('pending-doctor-appointments/', PendingDoctorAppointmentsView.as_view(),name='pending-doctor-appointments'),
    path('approved-doctor-appointments/', UpcomingDoctorAppointmentsView.as_view(),name='approved-doctor-appointments'),
    path('completed-doctor-appointments/', CompletedDoctorAppointmentsView.as_view(),name='completed-doctor-appointments'),
    path('get-doctor-appointment/<str:slug>/', DoctorDetailAppointmentView.as_view(),name='doctor-appointment-detail'),
    path('update-doctor-appointment/<str:slug>/', DoctorUpdateAppointmentView.as_view(),name='update-doctor-appointment'),
   
]

employee_patterns = [
    path('general-employee-view-for-all-employees/', GeneralEmployeeViewForNonDoctors.as_view(),name='general-employee-view-for-all-employees'),

]

urlpatterns = patient_patterns + doctor_patterns + admin_patterns + employee_patterns
