from django.contrib import admin

from tasks import models
# Register your models here.

class TaskDetailInfo(admin.ModelAdmin):
    list_display = ['name', 'owner', 'createdate', 'updatedate']

class TaskInfo(admin.ModelAdmin):
    list_display = ['name','status','category', 'taskdetail']

admin.site.register(models.Task, TaskInfo)
admin.site.register(models.TaskDetail, TaskDetailInfo)