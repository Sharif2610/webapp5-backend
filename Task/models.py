from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    #user = models.ForeignKey(User,on_delete=models.CASCADE) #if user del-> task also dele
    title = models.CharField(max_length=100)
    description = models.TextField() # if we want longer text
    deadline = models.DateTimeField() # here stores date + time for task deadline.
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)