from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Paragraph)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_number',
                    'paragraph',
                    'class_id',
                    'slug',
                    'task_title',
                    'task_description',
                    'task_snippet',
                    'author', )
    prepopulated_fields = {'slug': ('task_number', 'class_id', 'paragraph')}
    ordering = ('class_id', 'paragraph', 'task_number')
    list_filter = ('class_id', 'paragraph', 'class_homework')


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
