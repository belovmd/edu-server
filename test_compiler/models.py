from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

class Task(models.Model):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    TASK_TYPE = (
        ('lesson', 'Задача с уроков'),
        ('homework', 'Упражнение для самостоятельного решения')
    )

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
    class_homework = models.CharField(verbose_name="Тип задания",
                                      max_length=255,
                                      choices=TASK_TYPE,
                                      default='lesson')

    def get_absolute_url(self):
        return reverse('task_view', args=[self.slug])

    def __str__(self):
        return "Задача {}, параграф {}, класс {}".format(self.task_number,
                                                         self.paragraph,
                                                         self.class_id)


class School(models.Model):

    class Meta:
        verbose_name = 'Учреждение образования'
        verbose_name_plural = 'Учреждения образования'

    name = models.CharField(verbose_name='Название УО', max_length=255)
    slug = AutoSlugField(populate_from=['name'])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_view', args=[self.slug])


class Paragraph(models.Model):
    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'

    title = models.CharField(verbose_name='Название параграфа', max_length=255)
    paragraph_id = models.IntegerField(verbose_name='Номер параграфа')
    class_id = models.IntegerField(verbose_name='Класс')

    def __str__(self):
        return "Класс {}, параграф {}, {}".format(self.class_id,
                                                  self.paragraph_id,
                                                  self.title)