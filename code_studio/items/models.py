# from django.core.exceptions import ValidationError
# from django.db import models
# from django_resized import ResizedImageField
# import datetime
#
#
# def validate_only_one_instance(obj):
#     model = obj.__class__
#     if model.objects.count() > 2 and obj.id != model.objects.get().id:
#         raise ValidationError(f"Вы не можете создать больше 3 {model.__name__} instance")
#
#
# class Item(models.Model):
#     name = models.CharField('Название', max_length=50)
#     img = ResizedImageField(size=[1280, 1024], crop=['middle', 'center'], upload_to='media', default=None, blank=True, null=True)
#     created_at = models.DateTimeField(default=datetime.datetime.now)
#     title = models.CharField('Заголовок1', max_length=50, default=None)
#     title2 = models.CharField('Заголовок2', max_length=50, default=None)
#     title3 = models.CharField('Заголовок3', max_length=50, default=None)
#
#     def __str__(self):
#         return self.name
#
#
#     def clean(self):
#         validate_only_one_instance(self)
#
#
# class Point(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
#     text = models.TextField(max_length=100)
#
#     def __str__(self):
#         return self.text
