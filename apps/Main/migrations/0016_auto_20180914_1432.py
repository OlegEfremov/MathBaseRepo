# Generated by Django 2.0.2 on 2018-09-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_auto_20180914_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasknumber',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasknumbers', to='Main.Source'),
        ),
    ]
