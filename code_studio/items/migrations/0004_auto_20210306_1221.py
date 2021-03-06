# Generated by Django 3.1.7 on 2021-03-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210306_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description_page',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='keywords_page',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Keyword'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title2',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Заголовок2'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title3',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Заголовок3'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title_tag',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='title_tag'),
        ),
    ]
