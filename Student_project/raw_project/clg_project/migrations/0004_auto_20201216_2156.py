# Generated by Django 3.1.4 on 2020-12-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_project', '0003_auto_20201216_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poject',
            name='project_id',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
