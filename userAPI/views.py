from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets

# from advisor.serializers import DriverInfoSerializer
from . import serializers
from .models import User, BookingHistory
from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer
from .serializers import AvailableAdvisorSerializer, BookAdvisorSerializer
from .serializers import UserBookingHistorySerializer


class CustomPermissionsForPser(permissions.BasePermission):

    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if 'user_id' in request.session.keys():
            return request.method in self.allowed_methods


class UserRegistration(APIView):

    serializer_class = UserRegistrationSerializer

    def get(self, request, format=None):
        customers = User.objects.all()
        serializer = UserRegistrationSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            request.session['user_id'] = serializer.validated_data["user_id"]
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListOfAvailableAdvisor(APIView):

    serializer_class = AvailableAdvisorSerializer

    def get(self, request, format=None):
        field = '__all__'

        serializer = AvailableAdvisorSerializer(data=request.data)

        if serializer.is_valid():
            data = {
                "Availability : "
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAdvisor(APIView):

    serializer_class = BookAdvisorSerializer
    # permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def post(self,request, format=None):
        context = {
            'user_id': request.session['user_id'],
            'booking_time':request.session['booking_time']
            }
        serializer = BookAdvisorSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            data = {
                "Success": "booking Done"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingHistoryList(APIView):

    serializer_class = UserBookingHistorySerializer
    # permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def get(self, request, format=None):
        user_id = request.session['user_id']
        user = User.objects.get(pk=user_id)
        booking_history = BookingHistory.objects.filter(user_id=user)
        if len(booking_history) > 0:
            serializer = UserBookingHistorySerializer(booking_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {"No history": "You do not have any history of booking"}
            return Response(data)


class Logout(APIView):

    def get(self, request, format=None):
        del request.session['user_id']
        data = {'Logout': 'logged out successfully'}
        return Response(data, status=status.HTTP_200_OK)


class UserRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserRegistrationSerializer

