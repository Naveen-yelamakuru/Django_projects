# Generated by Django 3.1.4 on 2020-12-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clg_project', '0005_auto_20201216_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poject',
            name='project_id',
        ),
    ]