from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    task_number = models.CharField(verbose_name='Номер задачи', max_length=30)
    slug = models.SlugField(verbose_name='Код (создается автоматически)',
                            unique=True)
    task_title = models.CharField(verbose_name='Заголовок', max_length=255,
                                  blank=True, null=True)
    task_description = models.TextField(verbose_name='Текст задачи',
                                        blank=True, null=True)
    task_snippet = models.TextField(
        verbose_name='Предопределенный фрагмент кода',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class_id = models.IntegerField(verbose_name='Номер класса',
                                   blank=True, null=True)
    paragraph = models.IntegerField(verbose_name='Номер параграфа',
                                    default=0)

    def get_absolute_url(self):
        return reverse('task_view', args=[self.slug])
