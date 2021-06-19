from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from .serializers import WorkshopSerializer, EmployeeSerializer, TaskSerializer
from .models import Workshop, Employee, Task
from .permissions import IsOwnerOrReadOnly


# ***************** workshops views ***************** 
class WorkshopList(generics.ListCreateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the workshop created_by
        serializer.save(created_by=self.request.user)

class WorkshopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

# ***************** employees views ***************** 
class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # retrieve all employees of a specific workshop
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        return Employee.objects.filter(workshop=workshop)

    def perform_create(self, serializer): 
        # add the employee created_by and workshop
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        serializer.save(created_by=self.request.user, workshop=workshop)

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'employee_pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        return Employee.objects.filter(workshop=workshop)


# ***************** tasks views ***************** 
class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # retrieve all tasks of a specific workshop
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        return Task.objects.filter(workshop=workshop)

    def perform_create(self, serializer): 
        # add the task created_by and workshop
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        serializer.save(created_by=self.request.user, workshop=workshop)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        workshop = get_object_or_404(Workshop, pk=self.kwargs['pk'])
        return Task.objects.filter(workshop=workshop)


