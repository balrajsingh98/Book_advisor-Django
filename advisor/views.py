from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from functools import partial

from .models import Advisor
from .serializers import AddAdvisorSerializer


class CustomPermissions(permissions.BasePermission):

    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if 'Advisor_id' in request.session.keys():
            return request.method in self.allowed_methods

class AddAdvisor(APIView):

    serializer_class = AddAdvisorSerializer

    def get(self, request, format=None):

        Advisors = Advisor.objects.all()
        serializer = AddAdvisorSerializer(Advisors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddAdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


