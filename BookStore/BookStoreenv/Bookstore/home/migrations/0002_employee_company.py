# Generated by Django 3.1.6 on 2021-02-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.CharField(default='tcs', max_length=200),
        ),
    ]
