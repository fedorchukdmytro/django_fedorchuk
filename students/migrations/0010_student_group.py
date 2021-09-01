# Generated by Django 3.2.6 on 2021-08-30 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0011_alter_group_curator'),
        ('students', '0009_remove_student_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hui', to='group.group'),
        ),
    ]