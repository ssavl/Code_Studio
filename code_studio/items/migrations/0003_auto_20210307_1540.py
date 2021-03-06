# Generated by Django 3.1.7 on 2021-03-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20210307_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'Пункт для заголовка', 'verbose_name_plural': 'Пункты для заголовка'},
        ),
        migrations.AlterField(
            model_name='point',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='Для какого товара'),
        ),
    ]
