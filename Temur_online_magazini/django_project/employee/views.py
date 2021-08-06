from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import *
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data=serializer.validated_data
            user=User.objects.create(
                first_name=data['user']['first_name'],
                last_name=data['user']['last_name'],
                username=data['user']['username'],
                email=data['user']['email'],
                password=data['user']['password'],
            )
            user.save()
            employee=Employee.objects.create(
                user=user,
                phone=data['phone'],
                image=data['image'],
                adress=data['adress'],
            )
            employee.save()
            print(data)
            return Response({'status':'created'},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


