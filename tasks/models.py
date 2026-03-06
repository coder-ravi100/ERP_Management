from django.db import models
from accounts.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        {'Pending' , 'pending'},
        {'In Progress' , 'in progress'},
        {'Completed' , 'completed'},
    ]
    PRIORITY_CHOICES = [
        {'Low' , 'low'},
        {'Medium' , 'medium'},
        {'High' , 'high'},
    ]
    title = models.CharField(max_length = 200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,on_delete = models.CASCADE , related_name = 'tasks')
    assigned_by = models.ForeignKey(User,on_delete = models.CASCADE , related_name = 'create_tasks')
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES , default = 'Pending')
    priority = models.CharField(max_length = 20 , choices = PRIORITY_CHOICES)
    due_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title