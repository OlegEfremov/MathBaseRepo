# Generated by Django 2.0.2 on 2018-06-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_solution_folder_tasks_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution_folder',
            name='tasks_order',
            field=models.TextField(blank=True, default='{}'),
        ),
    ]
