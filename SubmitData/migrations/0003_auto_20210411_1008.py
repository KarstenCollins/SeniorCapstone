# Generated by Django 3.1.7 on 2021-04-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0002_auto_20210411_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='account_number',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='company_name',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
