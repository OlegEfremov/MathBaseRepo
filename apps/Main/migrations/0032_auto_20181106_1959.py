# Generated by Django 2.0.2 on 2018-11-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_auto_20181104_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
