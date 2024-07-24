from django.db import models
from django.utils import timezone


class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"

class Category(models.TextChoices):
    PROJECT = 'project', "Project Management"
    DAILYWORK = 'daily', "Daily Work"
    OTHER = 'other', "Other Task"


class TaskDetail(models.Model):
    name = models.CharField(max_length=64, default='undefined')
    owner = models.CharField(max_length=64, default='')
    createdate = models.DateTimeField(default=timezone.now)
    updatedate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name+'_'+self.owner
    
    def save(self):
        pass

    class Meta:
        verbose_name = '任务详情'
        verbose_name_plural = '任务详细信息'


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
    category = models.CharField(verbose_name="Task Category", max_length=10, choices=Category.choices)
#    pro = models.ForeignKey(to=TaskDetail, on_delete=models.CASCADE, verbose_name='Project', null = True)
    taskdetail = models.ForeignKey(to=TaskDetail, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = '任务信息'
        verbose_name_plural = '任务基本情况'


    def __str__(self):
        return self.name

