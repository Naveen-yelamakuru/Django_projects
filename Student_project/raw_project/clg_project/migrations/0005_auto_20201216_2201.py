# Generated by Django 3.1.4 on 2020-12-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_project', '0004_auto_20201216_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poject',
            name='project_id',
            field=models.IntegerField(default=1),
        ),
    ]