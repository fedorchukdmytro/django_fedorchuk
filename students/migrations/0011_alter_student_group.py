# Generated by Django 3.2.6 on 2021-08-30 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0011_alter_group_curator'),
        ('students', '0010_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_in_group', to='group.group'),
        ),
    ]
