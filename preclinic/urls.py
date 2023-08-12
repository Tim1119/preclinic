from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls',namespace='accounts')),
    path('profiles/', include('apps.profiles.urls',namespace='profiles')),
    path('utilities/', include('apps.utilities.urls',namespace='utilities')),
    path('appointments/', include('apps.appointments.urls',namespace='appointments')),
    path('ailment/', include('apps.ailment.urls',namespace='ailments')),
    path('course/', include('apps.course.urls',namespace='courses')),
    path('departments/', include('apps.departments.urls',namespace='departments')),
    path('institution/', include('apps.institution.urls',namespace='institutions')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

