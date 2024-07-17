from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse

# for chart
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io



# Create your views here.

def BasePage(request):
    if request.user.is_authenticated:
        Task = TaskDetails.objects.all()
        context = {
            'Task' : Task
        }
        return render(request, 'myapp/base.html', context)
    else:
        messages.error(request, 'You must be logged in to create a task')
        return redirect('login')
    

    return render(request, 'myapp/base.html')

def LoginView(request):
    
    if request.method == 'POST':   
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None: 
                login(request, user)
                messages.success(request, "You are successfully logged in.")
                return redirect('base')
            else:
                messages.error(request, "Input Username or Password Correctly.")
                
    else:
        form = LoginForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'myapp/login.html', context)
            
def LogoutView(request):
    logout(request)
    messages.success(request, "You are successfully logged out.")
    return redirect('login')
    
def RegisterView(request):
    if request.method == 'POST':   
        register_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        
        if register_form.is_valid() and userprofile_form.is_valid():
            user = register_form.save()
            user_profile = userprofile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
           
            messages.success(request, "You are successfully registered.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        register_form = RegisterForm()
        userprofile_form = UserProfileForm()
    
    context = {
        'register_form': register_form,
        'userprofile_form': userprofile_form,
    }
    
    return render(request, 'myapp/register.html', context)


def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('base')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'myapp/change_password.html', {'form': form})
        
def ShowProfile(request):
    if request.user.is_authenticated:
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        account = Account.objects.get(account_holder=user)
        context = {
            'userprofile': userprofile,
            'account': account
        }
        return render(request, 'myapp/userprofile.html', context)
    else:
        messages.success(request, 'You must be logged be')
        return redirect('login')
    
def Update_profile(request, id):
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(id=id)
        form = UserProfileForm(request.POST or None, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('show_profile')
        return render(request, 'myapp/update_profile.html', {'form':form})
       
    else:
        messages.error(request, 'Your have to login to update profile!')
        return render(request, 'myapp/update_profile.html')


def TaskDetail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskDetailForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.task_created = request.user
                task.save()
                messages.success(request, 'Task Created Successfully')
                return redirect('base')
            else:
                messages.error(request, 'There was an error creating the task')
        else:
            form = TaskDetailForm()
        return render(request, 'myapp/task_detail.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to create a task')
        return redirect('login')
    
        
def TaskInfo(request, id):
    if request.user.is_authenticated:
        task = TaskDetails.objects.get(id=id)
        context = {
            'task' : task,
        }
        return render(request, 'myapp/task_info.html', context)
    else:
        messages.error(request, 'You must be logged in to create a task')
        return redirect('login')

def Update_task(request, id):
    if request.user.is_authenticated:
        update_task = TaskDetails.objects.get(id=id)
        form = TaskDetailForm(request.POST or None, instance=update_task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('base')
        return render(request, 'myapp/update_task.html', {'form':form})
       
    else:
        messages.error(request, 'Your have to login to update task!')
        return render(request, 'myapp/update_task.html')
    
def Delete_task(request, id):
    if request.user.is_authenticated:
        task = TaskDetails.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('base')
    else:
        messages.error(request, 'You must be logged in to delete a task')
        return redirect('login')

def Accept_task(request, id):
    if request.user.is_authenticated:
        user = request.user
        task = TaskDetails.objects.get(id=id)
        task.task_status = 'In Process'
        task.save()
        Bucket(user=user, task=task).save()
        messages.success(request, 'Task Accepted Successfully')
        return redirect('bucket')
    else:
        messages.error(request, 'You must be logged in to accept a task')
        return redirect('login')
    
def showbucket(request):
    if request.user.is_authenticated:
        user = request.user
        bucket = Bucket.objects.filter(user=user)
        return render(request, 'myapp/bucket.html',  {
            'bucket' : bucket,
        })
    
    else:
        messages.error(request, 'You must be logged in to accept a task')
        return redirect('login')

def remove_task(request, id):
    if request.user.is_authenticated:
        task = TaskDetails.objects.get(id=id)
        task.task_status = 'Open'
        task.save()
        bucket = Bucket.objects.filter(task=id)
        bucket.delete()
        messages.success(request, 'Task Removed Successfully')
        return redirect('bucket')
    else:
        messages.error(request, 'You must be logged in to remove a task')
        return redirect('login')
     
def closed_task(request, id):
    if request.user.is_authenticated: 
        user = request.user
        task = TaskDetails.objects.get(id=id)
        task.task_status = 'Close'
        task.task_closed = user
        task.task_closed_on = timezone.now()
        task.save()
        bucket = Bucket.objects.filter(task=id)
        bucket.delete()
        messages.success(request, 'Task Closed Successfully')
        return redirect('bucket')
    else:
        messages.error(request, 'You must be logged in to close a task')
        return redirect('login')

def reopen_task(request, id):
    if request.user.is_authenticated:
        user = request.user
        task = TaskDetails.objects.get(id=id)
        task.task_status = 'Reopen'
        holder = User.objects.get(username=task.task_closed)
        task.save()
        Bucket(user=holder, task=task).save()
        messages.success(request, 'Task Reopened Successfully')
        return redirect('base')
    else:
        messages.error(request, 'You must be logged in to reopen a task')
        return redirect('login')
    
def resolve_task(request, id):
    if request.user.is_authenticated:
        task = TaskDetails.objects.get(id=id)
        task.task_status = 'Resolved'
        task.save()
        creator = get_object_or_404(Account, account_holder = task.task_created)
        resolver = get_object_or_404(Account, account_holder = task.task_closed)

        if creator.account_balance >= task.task_reward:
            creator.account_balance -= task.task_reward
            creator.save()
            resolver.account_balance += task.task_reward
            resolver.save()
            Transaction.objects.create(sender =  task.task_created, receiver = task.task_closed, amount = task.task_reward)

        messages.success(request, 'Task Resolved Successfully')
        return redirect('base')
    else:
        messages.error(request, 'You must be logged in to reopen a task')
        return redirect('login')

def Account_Detail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Coin Added Successfully')
                return redirect('base')
        else:
            form = AccountForm()
            return render(request, 'myapp/account.html', {'form':form})
    else:
        messages.error(request, 'You must be logged in to add coin')
        return redirect('login')
    
def Transactions(request):
    if request.user.is_authenticated:
        user = request.user
        transactions = Transaction.objects.filter(Q(sender=user)|Q(receiver=user))
        context = {
            'transactions': transactions,
        }
        return render(request, 'myapp/transaction.html', context)
    else:
        messages.error(request, 'You must be logged in to see transaction')
        return redirect('login')


# Chart 
def dashboard(request):
    if request.user.is_authenticated:

        open = TaskDetails.objects.filter(task_status='Open').count()
        close = TaskDetails.objects.filter(task_status='Closed').count()
        inprocess = TaskDetails.objects.filter(task_status='Inprocess').count()
        reopen = TaskDetails.objects.filter(task_status='Reopen').count()
        expired = TaskDetails.objects.filter(task_status='Expired').count()
        resolved = TaskDetails.objects.filter(task_status='Resolved').count()

        status_task = {
            'open': open,
            'close': close,
            'inprocess': inprocess,
            'reopen': reopen,
            'expired': expired,
            'resolved': resolved,
        }
        
        labels = status_task.keys()
        count = status_task.values()

        plt.figure(figsize=(6,5))
        plt.pie(count, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Task Status Pie Chart')
        buffer=io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return HttpResponse(buffer, content_type='image/png')


    else:
        messages.error(request, 'You must be logged in to see the dashboard')
        return redirect('login')
    
def chart_show(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/task_status.html')

    else:
        messages.error(request, 'You must be logged in to see the dashboard')