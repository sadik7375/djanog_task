import genericpath
from django.shortcuts import render,redirect
from rest_framework import generics
from .serializers import *
from .models import *
from django.views.generic import TemplateView


class ListTask(generics.ListAPIView): 

       queryset=Task_list.objects.all()
       serializer_class=TaskSerializer
              

class DetailTask(generics.RetrieveUpdateAPIView):
       queryset=Task_list.objects.all()
       serializer_class=TaskSerializer


class CreateTask(generics.CreateAPIView):  
       queryset=Task_list.objects.all()
       serializer_class=TaskSerializer

class DeleteTask(generics.DestroyAPIView):  
       queryset=Task_list.objects.all()
       serializer_class=TaskSerializer
       def destroy(self, request, *args, **kwargs):
           response = super().destroy(request, *args, **kwargs)
           return redirect('task_list')  # Assuming 'task_list' is the name of your task list view


class TaskListView(TemplateView):
    template_name = 'task_list/tasks_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task_list.objects.all()
        return context