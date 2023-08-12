from django.urls import path
from .views import (AllDepartmentsView,CreateDepartmentView,UpdateDepartmentView,DeleteDepartmentView)


app_name = 'departments'

urlpatterns = [
    path('all-departments/', AllDepartmentsView.as_view(),name='all-departments'),
    path('create-department/',CreateDepartmentView.as_view(),name='create-department'),
    path('update-department/<str:slug>/', UpdateDepartmentView.as_view(),name='update-department'),
    path('delete-department/<str:slug>/',DeleteDepartmentView.as_view(),name='delete-department'),
 
]

