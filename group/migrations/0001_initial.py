# Generated by Django 3.2.6 on 2021-08-07 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descipline', models.CharField(max_length=200)),
                ('hours_to_take', models.IntegerField(validators=[django.core.validators.MaxValueValidator(30)])),
            ],
        ),
    ]
