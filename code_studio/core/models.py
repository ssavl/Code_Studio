from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
import random
from django_resized import ResizedImageField



class HomePage(models.Model):
    keywords_page = models.CharField('Keyword', max_length=50, default=None)
    description_page = models.CharField('Description', max_length=50, default=None)
    title_tag = models.CharField('title_tag', max_length=50, default=None)
    title = models.CharField('Заголовок главной страницы', max_length=50, default=None)
    first_img = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
    second_img = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
    third_img = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
    fourth_img = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
    latitude = models.CharField('Широта', max_length=20, default=None)
    longitude = models.CharField('Долгота', max_length=20, default=None)
    text = models.TextField("Текст под слайдером", max_length=500, default=None)


    def __str__(self):
        return f"Главная страница_#{random.randint(1, 999)}"





