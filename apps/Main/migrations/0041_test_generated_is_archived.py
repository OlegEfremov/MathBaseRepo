# Generated by Django 2.0.2 on 2018-12-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0040_test_template_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_generated',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
