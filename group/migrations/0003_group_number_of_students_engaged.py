# Generated by Django 3.2.6 on 2021-09-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20210902_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='number_of_students_engaged',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]