# Generated by Django 5.1 on 2024-09-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='Дата окончания'),
        ),
    ]
