# Generated by Django 3.2.6 on 2021-09-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20210906_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='sub',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
