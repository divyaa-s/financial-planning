# myapp/urls.py
from django.urls import path
from .views import *


urlpatterns =[
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('patients/', patients, name='patients'),
    path('emergency/', fgcs_emergency, name='emergency'),
    path('heart_rate/', fgcs_heart, name='heartRate'),
    path('bp/', fgcs_bp, name='bp'),
    path('oxSat/', fgcs_spo2, name='oxSat'),
    path('pulse/', fgcs_pulse, name='pulse'),
    path('stepCount/', fgcs_step, name='stepCount'),
    path('skinTemp/', fgcs_skin, name='skinTemp'),
    path('form/',form,name='form'),
    #path('profile/',profile,name='profile'),
    path('patient/<int:patient_id>/', patient_info, name='patient_info'),

]


