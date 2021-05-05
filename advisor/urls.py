from django.urls import path
from . import views

app_name = 'advisor'

urlpatterns = [

    path('register/', views.AddAdvisor.as_view(), name='Add_Advisor'),
   ]
