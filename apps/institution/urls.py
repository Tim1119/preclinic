from django.urls import path
from .views import (AllInstitutionsView,CreateInstitutionView,UpdateInstitutionView,DeleteInstitutionView)


app_name = 'institutions'

urlpatterns = [
    path('all-institutions/', AllInstitutionsView.as_view(),name='all-institutions'),
    path('create-institution/',CreateInstitutionView.as_view(),name='create-institution'),
    path('update-institution/<str:slug>/', UpdateInstitutionView.as_view(),name='update-institution'),
    path('delete-institution/<str:slug>/',DeleteInstitutionView.as_view(),name='delete-institution'),
 
]

