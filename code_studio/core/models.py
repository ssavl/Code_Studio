from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
import random
from django_resized import ResizedImageField
from django.core.validators import FileExtensionValidator



class HomePage(models.Model):

    keywords_page = models.CharField('Ключевые слова', max_length=50, default=None, blank=True)
    description_page = models.CharField('Описание', max_length=50, default=None, blank=True)
    title_tag = models.CharField('Тэг', max_length=50, default=None, blank=True)
    title = models.CharField('Заголовок главной страницы', max_length=50, default=None)
    first_img = ResizedImageField('Первое изображение слайдера', size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg')
        ])
    second_img = ResizedImageField('Второе изображение слайдера', size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg')
        ])
    third_img = ResizedImageField('Третье изображение слайдера', size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg')
        ])
    fourth_img = ResizedImageField('Четвертое изображение слайдера', size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg')
        ])
    latitude = models.CharField('Широта', max_length=20, default=None, blank=True)
    longitude = models.CharField('Долгота', max_length=20, default=None, blank=True)
    text = models.TextField("Текст под слайдером", max_length=500, default=None, blank=True)

    class Meta:
        verbose_name = 'Домашняя страница'
        verbose_name_plural = 'Домашняя страница'



    def __str__(self):
        return f"Домашняя страница"





