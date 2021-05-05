from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advisor.models import Advisor
from . import models
from .models import User , BookingHistory


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email and password:
            raise ValidationError("Username and Password is required")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("This email address does not exist")
        if user.password == password:
            data["user_id"] = user.id
            return data
        else:
            raise ValidationError("Invalid credentials")

class AvailableAdvisorSerializer(serializers.Serializer):

    def validate(self, data):
        return data
    count=0
    data = [0, 1, 10, -5]
    for i in data:
        if i > 0 :
            count=+1
            print(count)
        else:
            print(0)




class UserBookingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingHistory
        fields = ['booking_time',
                  'booking_id']


class BookAdvisorSerializer(serializers.Serializer):
    booking_id = serializers.CharField()

    def validate(self, data):
        booking_id = data.get("booking_id")
        booking_time = models.DateTimeField(auto_now_add=True)

        if not booking_id:
            raise ValidationError("Number is required")
        try:
            advisor = Advisor.objects.get(booking_id=booking_id)
        except Advisor.DoesNotExist:
            raise ValidationError("does not exist")

        return data

    def create(self, validated_data):
        booking_id = validated_data.pop('booking_id')
        user_id = self.context.get("user_id")
        user = User.objects.get(pk=user_id)
        advisor = Advisor.objects.get(booking_id=booking_id)
        obj1 = BookingHistory()
        obj1.user_id = user
        obj1.advisor_id = advisor
        obj1.booking_id = advisor.booking_id
        obj1.save()
        obj.advisor_id = advisor
        obj.booking_id = booking_id
        obj.user_name = user.name
        obj.save()
        return obj


class UserProfileSerializer(serializers.ModelSerializer):

    model = User
    fields = '__all_'