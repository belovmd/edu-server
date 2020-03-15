# Generated by Django 3.0.2 on 2020-03-15 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('task_title', models.CharField(blank=True, max_length=30, null=True)),
                ('task_description', models.TextField()),
                ('task_snippet', models.TextField(blank=True, null=True)),
                ('class_id', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
