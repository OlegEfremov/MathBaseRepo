# Generated by Django 2.0.2 on 2018-12-20 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0042_test_folder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star_Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkbox_values', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('solutions', models.ManyToManyField(blank=True, related_name='star_folders', to='Main.Solution')),
                ('tasks', models.ManyToManyField(blank=True, related_name='star_folders', to='Main.Task')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
