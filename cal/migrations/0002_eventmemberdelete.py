# Generated by Django 3.1.7 on 2021-05-20 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMemberDelete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cal.event')),
            ],
            options={
                'unique_together': {('event',)},
            },
        ),
    ]
