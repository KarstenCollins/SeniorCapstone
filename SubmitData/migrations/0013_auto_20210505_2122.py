# Generated by Django 3.1.7 on 2021-05-06 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0012_merge_20210505_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_entered']},
        ),
    ]
