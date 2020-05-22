from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    task_number = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    task_title = models.CharField(max_length=30, blank=True, null=True)
    task_description = models.TextField(blank=True, null=True)
    task_snippet = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class_id = models.IntegerField(blank=True, null=True)
    paragraph = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('task_view', args=[self.slug])
