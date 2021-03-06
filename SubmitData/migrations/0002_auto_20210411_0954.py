# Generated by Django 3.1.7 on 2021-04-11 16:54

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='date_entered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='account_number',
            field=models.CharField(default='Default', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='company_name',
            field=models.CharField(default='Default', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='statement_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
