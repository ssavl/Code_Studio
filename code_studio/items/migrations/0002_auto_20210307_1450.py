# Generated by Django 3.1.7 on 2021-03-07 14:50

import datetime
import django.core.validators
from django.db import migrations, models
import django_resized.forms
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_page',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 1024], upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg'), items.models.FileValidator(max_size=2097152)], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='keywords_page',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title_tag',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='point',
            name='text',
            field=models.TextField(max_length=100, verbose_name='Текст заголовка'),
        ),
        migrations.AlterField(
            model_name='point',
            name='title_num',
            field=models.CharField(choices=[('1', 'Для первого заголовка'), ('2', 'Для второго заголовка'), ('3', 'Для третьего заголовка')], max_length=1, verbose_name='Для какого заголовка'),
        ),
    ]