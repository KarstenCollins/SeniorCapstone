# Generated by Django 3.1.7 on 2021-04-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncomeInformation', '0003_auto_20210429_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date_received',
            field=models.CharField(max_length=12),
        ),
    ]