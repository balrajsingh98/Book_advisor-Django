from django.db import models
from advisor.models import Advisor
# Create your models here.
from django.db.models import DecimalField


class User(models.Model):

    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)


class BookingHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    picture = models.ImageField
    advisor_id = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=50)


