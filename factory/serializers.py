from rest_framework import serializers
from .models import Workshop, Employee, Task


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    workshop = serializers.ReadOnlyField(source='workshop.name')

    class Meta:
        model = Task
        fields = ['id', 'name', 'created_by', 'workshop'] 


class EmployeeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    workshop = serializers.ReadOnlyField(source='workshop.name')

    class Meta:
        model = Employee
        fields = ['id', 'username', 'created_by', 'workshop'] 


class WorkshopSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    employees = EmployeeSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = ['id', 'name', 'employees', 'tasks', 'created_by'] 

