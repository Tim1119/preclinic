from django.urls import path,include
from .views import (AllCoursesView,CreateCourseView,UpdateCourseView,DeleteCourseView)


app_name = 'courses'

urlpatterns = [
    path('all-courses/', AllCoursesView.as_view(),name='all-courses'),
    path('create-course/',CreateCourseView.as_view(),name='create-course'),
    path('update-course/<str:slug>/', UpdateCourseView.as_view(),name='update-course'),
    path('delete-course/<str:slug>/',DeleteCourseView.as_view(),name='delete-course'),
 
]

