# Generated by Django 3.0.6 on 2020-05-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_compiler', '0006_task_class_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название главы')),
                ('paragraph_id', models.IntegerField(verbose_name='название главы')),
                ('class_id', models.IntegerField(verbose_name='класс')),
            ],
        ),
    ]
