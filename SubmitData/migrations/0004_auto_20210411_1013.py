# Generated by Django 3.1.7 on 2021-04-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0003_auto_20210411_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='account_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='company_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
