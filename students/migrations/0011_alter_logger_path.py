# Generated by Django 3.2.6 on 2021-10-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20211016_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='path',
            field=models.CharField(max_length=30),
        ),
    ]
