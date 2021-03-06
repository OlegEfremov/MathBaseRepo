# Generated by Django 2.0.2 on 2018-06-05 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT_SOLUTION_NAME', max_length=200)),
                ('body', models.TextField(blank=True)),
                ('mathAttribute', models.ManyToManyField(blank=True, related_name='solutions', to='Main.MathAttribute')),
            ],
        ),
        migrations.CreateModel(
            name='Solution_Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT_FOLDER_NAME', max_length=200)),
                ('system_name', models.CharField(default='DEFAULT_FOLDER_SYSTEM_NAME', max_length=200)),
                ('task_order', models.TextField(blank=True, default='')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfolders', to='Main.Solution_Folder')),
                ('solution', models.ManyToManyField(blank=True, related_name='solution_folders', to='Main.Solution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT', max_length=200)),
                ('info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('ans', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('source', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasknumbers', to='Main.Source')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='taskNumber',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='Main.TaskNumber'),
        ),
        migrations.AddField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='Main.Task'),
        ),
    ]
