# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-19 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150511_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('term_id', models.CharField(max_length=500, primary_key=True, serialize=False, verbose_name='Ідентифікатор терміну')),
                ('term', models.TextField(verbose_name='Термін')),
                ('translation', models.TextField(verbose_name='Переклад')),
                ('source', models.CharField(choices=[('g', 'Google translate'), ('p', 'Translations from PEP project'), ('t', 'Translator of declarations project')], max_length=1, verbose_name='Джерело перекладу')),
                ('quality', models.IntegerField(verbose_name="Суб'єктивна якість перекладу")),
                ('strict_id', models.BooleanField(verbose_name='Чи було ідентифікатор спрощено')),
            ],
        ),
    ]
