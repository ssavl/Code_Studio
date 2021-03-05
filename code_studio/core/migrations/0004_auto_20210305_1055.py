# Generated by Django 3.1.7 on 2021-03-05 10:55

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210304_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='first_img',
            field=models.ImageField(default=None, upload_to='', verbose_name=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1280, 860], upload_to='media')),
        ),
    ]