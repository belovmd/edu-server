# Generated by Django 3.0.6 on 2020-05-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_compiler', '0008_auto_20200523_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='class_id',
            field=models.IntegerField(verbose_name='кКласс'),
        ),
    ]
