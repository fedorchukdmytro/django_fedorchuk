# Generated by Django 3.2.6 on 2021-08-29 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('group', '0010_alter_group_curator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]
