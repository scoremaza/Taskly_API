from django.contrib import admin
from .models import TaskList, Task, Attachment


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')
