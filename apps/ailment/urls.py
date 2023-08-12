from django.urls import path,include
from .views import (AllAilmentsView,CreateAilmentsView,UpdateAilmentsView,DeleteAilmentsView
                    )


app_name = 'ailments'

urlpatterns = [
    path('all-ailments/', AllAilmentsView.as_view(),name='all-ailments'),
    path('create-ailment/', CreateAilmentsView.as_view(),name='create-ailment'),
    path('update-ailment/<str:slug>/', UpdateAilmentsView.as_view(),name='update-ailment'),
    path('delete-ailment/<str:slug>/', DeleteAilmentsView.as_view(),name='delete-ailment'),
 
]

