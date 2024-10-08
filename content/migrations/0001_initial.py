# Generated by Django 5.1 on 2024-09-22 15:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Котегория',
                'verbose_name_plural': 'Котегории',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название видеоматериала')),
                ('content', models.FileField(upload_to='content/$Y/%m/%d/', verbose_name='Видеоконтент')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Уникальный идндефикатор')),
                ('pub_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')),
                ('author_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('categories_content', models.ManyToManyField(blank=True, null=True, related_name='categories_content', to='content.category')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
            },
        ),
    ]
