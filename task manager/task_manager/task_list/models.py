from django.db import models
from django.contrib.auth.models import User
class Task_list(models.Model):
    
        Title = models.CharField(max_length=100, blank=False)
        Description = models.TextField(blank=True)
        Data = models.DateField(blank=True)
        completed = models.BooleanField(default=False)



        def __str__(self):
                return self.Title

