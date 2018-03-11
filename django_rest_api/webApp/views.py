from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializer import employeesSerializer

# Lists all employees or create a new one
#employees/

class EmployeeList(APIView):

    def get(self,request):
        employee = employees.objects.all()
        serializer = employeesSerializer(employee, many=True)
        return Response(serializer.data)


