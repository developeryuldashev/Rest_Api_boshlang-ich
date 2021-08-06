from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

class EmployeeSerializer(serializers.ModelSerializer):
    user=UserSerializer(required=False)
    class Meta:
        model=Employee
        fields='__all__'
