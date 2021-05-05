# Generated by Django 3.1.7 on 2021-05-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubmitData', '0010_auto_20210504_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='adjustment',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='credits',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='interest_charges',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='late_fees',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='payments',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='previous_balance',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
