from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Address
    
class TaskDetails(models.Model):
    task_title = models.CharField(max_length=100)
    task_created = models.ForeignKey(User, related_name='created', on_delete=models.CASCADE)
    task_closed = models.ForeignKey(User, related_name='closed', null=True, blank=True, on_delete=models.CASCADE)
    task_created_on = models.DateField(auto_now_add=True, blank=True)
    task_closed_on = models.DateField(null=True)
    task_due_date = models.DateField()
    task_reward = models.IntegerField()
    task_description = models.CharField(max_length=1000)
    task_holder = models.CharField(max_length=100, null=True)
    choice = [('Open', 'Open'), ('Inprocess', 'Inprocess'), ('Closed', 'Closed'), ('Reopen', 'Reopen'), ('Expired', 'Expired')]
    task_status = models.CharField(max_length=100, choices=choice, default='Open')

    class Meta:
        verbose_name_plural = "Task Details"

class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskDetails, on_delete=models.CASCADE)
    task_count = models.IntegerField(default=1)

class Account(models.Model):
    account_holder = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.IntegerField()

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    
