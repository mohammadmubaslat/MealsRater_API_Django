from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task


class GetTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    # retrieve means: return one item only
class SingleTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# queryset: if i retrun anything --> here i don't return anything so i don't need it
class AddTask(generics.CreateAPIView):
    serializer_class = TaskSerializer


class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
