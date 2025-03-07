# Generated by Django 2.2.10 on 2020-03-16 18:40

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_pages', '0025_auto_20200220_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawhtmlpage',
            name='body_en',
            field=models.TextField(default='', verbose_name='[UA] Текст сторінки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawhtmlpage',
            name='title_en',
            field=models.CharField(default='', max_length=255, verbose_name='[EN] Заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticpage',
            name='body_en',
            field=wagtail.core.fields.RichTextField(default='', verbose_name='[EN] Текст сторінки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticpage',
            name='title_en',
            field=models.CharField(default='', max_length=255, verbose_name='[EN] Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rawhtmlpage',
            name='body',
            field=models.TextField(verbose_name='[UA] Текст сторінки'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='body',
            field=wagtail.core.fields.RichTextField(verbose_name='[UA] Текст сторінки'),
        ),
    ]
