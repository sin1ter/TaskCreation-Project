from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.BasePage, name='base'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView, name='register'),
    
    # Change Password
    path('change_password/', views.ChangePassword, name='change_password'),
    
    # Forget Password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='myapp/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),

    path('profile/', views.ShowProfile, name='profile'),
    path('udpate_profile/<int:id>/', views.Update_profile, name='udpate_profile'),

    path('taskdetails/', views.TaskDetail, name='taskdetails'),
    path('taskinfo/<int:id>/', views.TaskInfo, name='taskinfo'),
    path('update_task/<int:id>/', views.Update_task, name='update_task'),
    path('delete_task/<int:id>/', views.Delete_task, name='delete_task'),
    path('accept_task/<int:id>/', views.Accept_task, name='accept_task'),
    path('bucket/', views.showbucket, name='bucket'),
    path('remove_task/<int:id>/', views.remove_task, name='remove_task'),
    path('closed_task/<int:id>/', views.closed_task, name='closed_task'),
    path('reopen_task/<int:id>/', views.reopen_task, name='reopen_task'),
    path('resolve_task/<int:id>/', views.resolve_task, name='resolve_task'),
    path('account/', views.Account_Detail, name='account'),
    path('transaction/', views.Transactions, name='transaction'),
        
    
]