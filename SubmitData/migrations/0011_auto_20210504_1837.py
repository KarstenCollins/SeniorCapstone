# Generated by Django 3.1.7 on 2021-05-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0010_auto_20210504_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_paid',
            field=models.BooleanField(default=0, help_text='Everything below is optional. These are recommended to be filled out if using a credit card'),
        ),
    ]