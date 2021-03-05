from django.core.exceptions import ValidationError
from django.db import models
from django_resized import ResizedImageField
import datetime




class Item(models.Model):
    keywords_page = models.CharField('Keyword', max_length=50, default=None)
    description_page = models.CharField('Description', max_length=50, default=None)
    title_tag = models.CharField('title_tag', max_length=50, default=None)
    name = models.CharField('Название', max_length=50)
    img = ResizedImageField(size=[1280, 1024], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField('Заголовок1', max_length=50, default=None, null=True)
    title2 = models.CharField('Заголовок2', max_length=50, default=None, null=True)
    title3 = models.CharField('Заголовок3', max_length=50, default=None, null=True)

    def __str__(self):
        return self.name



class Point(models.Model):
    title_num_choises = [
        ('1', 'first'),
        ('2', 'second'),
        ('3', 'third')
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    title_num = models.CharField(max_length=1, choices=title_num_choises)
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text
