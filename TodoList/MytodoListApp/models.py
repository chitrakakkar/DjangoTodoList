from django.db import models
from django.utils import timezone


#  Table name, has to wrap models.Model to get the functionality of Django.

class todo(models.Model):
    # Task_name will be our task title. Allow only 10 chars.
    # Setting as unique constrain to avoid two tasks with the same name.
    task_name = models.CharField(max_length=100, null=True)
    task_description = models.TextField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# Returning the name of the task
    # def __unicode__(self):
    #     return self.task_name

# Telling Django to ordered our tasks by date
    class Meta:
        ordering = ['date_created']
