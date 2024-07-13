from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
class UserProfileForm(forms.ModelForm):
    
    Address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    City = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    State = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta: 
        model = UserProfile
        fields = ('Address', 'City', 'State')


class TaskDetailForm(forms.ModelForm):

    task_title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    task_due_date = forms.DateField(label = 'Task Due Date')
    task_reward = forms.IntegerField(label = 'Task Reward')
    task_description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TaskDetails
        fields = ('task_title', 'task_due_date', 'task_reward', 'task_description')
        
    
class AccountForm(forms.ModelForm):
    
    account_holder = forms.ModelChoiceField(label='Account Holder', queryset=User.objects.all())
    account_balance = forms.IntegerField(label='Account Balance', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta: 
        model = Account
        fields = ('account_holder', 'account_balance')