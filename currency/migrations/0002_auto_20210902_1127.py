# Generated by Django 3.2.6 on 2021-09-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='source',
        ),
        migrations.AddField(
            model_name='exchange',
            name='bank',
            field=models.CharField(default='privatbank', max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='buy_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='currency',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='sale_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]