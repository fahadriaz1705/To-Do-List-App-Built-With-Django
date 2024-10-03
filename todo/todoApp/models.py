from django.db import models

# Create your models here.
class Task(models.Model):
    taskId = models.AutoField
    taskName = models.TextField(max_length='50',default='')
    desc = models.TextField(max_length= "200",default='')
    date = models.DateTimeField()
    userN = models.TextField(max_length=30,default='')

    def __str__(self):
        return self.taskName
