# Generated by Django 3.2.6 on 2021-09-02 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20210902_1127'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=6)),
                ('path', models.CharField(max_length=20)),
                ('execution_time', models.DecimalField(decimal_places=10, max_digits=15)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_in_group', to='group.group'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
