# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 16:55
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifySend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='Адреса')),
                ('error', models.CharField(blank=True, default='', max_length=250, verbose_name='Помилки відправки')),
                ('found_new', models.IntegerField(default=0, verbose_name='Знайдено нових')),
                ('new_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), blank=True, default=[], size=None, verbose_name='Нові документи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створений')),
            ],
        ),
        migrations.CreateModel(
            name='SearchTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=150, verbose_name='Пошуковий запит')),
                ('deepsearch', models.BooleanField(default=False, verbose_name='Шукати скрізь')),
                ('query_params', models.TextField(blank=True, default='', max_length=500, verbose_name='Опції')),
                ('is_enabled', models.BooleanField(db_index=True, default=True, verbose_name='Активний')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Видалений')),
                ('found_total', models.IntegerField(default=0, verbose_name='Знайдено всього')),
                ('found_week', models.IntegerField(default=0, verbose_name='Знайдено за тиждень')),
                ('found_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), blank=True, default=[], size=None, verbose_name='Знайдені документи')),
                ('last_run', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Останній запуск')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створений')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found_total', models.IntegerField(default=0, verbose_name='Знайдено всього')),
                ('found_new', models.IntegerField(default=0, verbose_name='Знайдено нових')),
                ('found_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), blank=True, default=[], size=None, verbose_name='Знайдені документи')),
                ('new_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), blank=True, default=[], size=None, verbose_name='Нові документи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створений')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotter.SearchTask')),
            ],
        ),
        migrations.AddField(
            model_name='notifysend',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotter.SearchTask'),
        ),
    ]
