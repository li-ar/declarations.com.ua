# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-19 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0017_reduce_focal_point_key_max_length'),
        ('cms_pages', '0022_homepage_youtube_embed_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='branding_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Зображення брендінгу'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='branding_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Посилання для переходу по кліку на брендінг'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='branding_slug',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ідентифікатор рекламної кампанії'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='youtube_embed_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Embed для youtube'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='youtube_embed_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок youtube відео'),
        ),
    ]
