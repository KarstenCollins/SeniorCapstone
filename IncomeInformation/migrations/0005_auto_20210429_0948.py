# Generated by Django 3.1.7 on 2021-04-29 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncomeInformation', '0004_auto_20210429_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date_received',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
