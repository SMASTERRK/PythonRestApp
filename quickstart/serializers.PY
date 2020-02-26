from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Employee, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['employeeid', 'employeename', 'squadname', 'project']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['employeename', 'jiraid']