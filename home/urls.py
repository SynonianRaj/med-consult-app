
from django.urls import path
from .views import homeview,choose_services,doctor_list

urlpatterns =[
    path('', homeview, name='home-view'),
    path('choose-services', choose_services,name="choose-services"),
    path('doctor-list/<str:id>',doctor_list,name="find-doctor"),
]