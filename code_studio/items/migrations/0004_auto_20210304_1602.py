# Generated by Django 3.1.7 on 2021-03-04 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210304_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
