from django.contrib import admin
from .models import User, BookingHistory
# Register your models here.

admin.site.register(User)
admin.site.register(BookingHistory)
# admin.site.register(RequestedCab)
