# Generated by Django 3.2.11 on 2022-03-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-20'),
            preserve_default=False,
        ),
    ]
