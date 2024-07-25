from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('Address', 'City', 'State')

class TaskDetailsAdmin(admin.ModelAdmin):
     list_display = (
        'task_title', 'task_created', 'task_closed', 
        'task_created_on', 'task_closed_on', 'task_due_date', 
        'task_reward', 'task_description', 'task_holder', 'task_status'
    )

class BucketAdmin(admin.ModelAdmin):
     list_display = (
          'user', 'task', 'task_count'
     )

class AccountAdmin(admin.ModelAdmin):
     list_display = (
          'account_holder', 'account_balance'
     )

class TransactionAdmin(admin.ModelAdmin):
     list_display = (
          'sender', 'receiver', 'amount', 'timestamp'
     )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(TaskDetails, TaskDetailsAdmin)
admin.site.register(Bucket, BucketAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)