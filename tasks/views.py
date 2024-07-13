from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def index(request):
    return render(request, 'tasks/index.html')

def add_task(request):
    return render(request, 'tasks/add_task.html')

def edit_task(request):
    return render(request, 'tasks/edit_task.html')