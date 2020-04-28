# Generated by Django 2.0.2 on 2020-04-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0048_test_generated_open_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedSolImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sol_images/')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.Solution')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedTaskImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='task_images/')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.Task')),
            ],
        ),
        migrations.AlterField(
            model_name='test_template',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='test_template',
            name='folders_and_numbers',
            field=models.TextField(blank=True, default='', verbose_name='Папки и номера задач'),
        ),
        migrations.AlterField(
            model_name='test_template',
            name='is_permanent',
            field=models.BooleanField(default=True, verbose_name='Постоянно'),
        ),
        migrations.AlterField(
            model_name='test_template',
            name='name',
            field=models.CharField(default='DEFAULT_TEST_TEMPLATE', max_length=1000, verbose_name='Имя шаблона'),
        ),
    ]