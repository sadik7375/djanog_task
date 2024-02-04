from rest_framework import serializers
from .models import Task_list

class TaskSerializer(serializers.ModelSerializer):
       
          class Meta:
           model=Task_list
           fields=('id','Title','Description','Data','completed')