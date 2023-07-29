from django.contrib import admin

from apps.tasks.models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', '_order', 'title', 'user', 'creation_date', 'due_date',
                    'priority', 'complete', 'is_attached', 'category')
    list_filter = ('user', 'category')


admin.site.register(Tasks, TasksAdmin)
