# Generated by Django 3.1.7 on 2021-03-04 15:07

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210304_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='first_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 860], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='fourth_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 860], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 860], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='third_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 860], upload_to='media'),
        ),
    ]