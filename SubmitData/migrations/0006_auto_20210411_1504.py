# Generated by Django 3.1.7 on 2021-04-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0005_post_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_paid',
            field=models.BooleanField(default=0),
        ),
    ]
