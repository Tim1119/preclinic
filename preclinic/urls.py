from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls',namespace='accounts')),
    path('profiles/', include('apps.profiles.urls',namespace='profiles')),
    path('utilities/', include('apps.utilities.urls',namespace='utilities')),
]
