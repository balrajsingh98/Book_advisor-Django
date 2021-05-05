from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Advisor


class AddAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

