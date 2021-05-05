from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'userAPI'

router = DefaultRouter()
router.register('profile', views.UserRegistrationViewSet,basename='profile')

urlpatterns = [

    path('register/', views.UserRegistration.as_view(), name='user-registration'),
    path('login/', views.UserLogin.as_view(), name='user-login'),
    path('logout/', views.Logout.as_view(), name='user-logout'),
    path('advisor/', views.ListOfAvailableAdvisor.as_view()),

    path('bookadvisor/', views.BookAdvisor.as_view(), name='booking'),
    path('bookinghistory/', views.BookingHistoryList.as_view(), name='bookinghistory')

]