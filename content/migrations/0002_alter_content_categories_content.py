# Generated by Django 5.1 on 2024-09-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='categories_content',
            field=models.ManyToManyField(blank=True, related_name='categories_content', to='content.category'),
        ),
    ]
