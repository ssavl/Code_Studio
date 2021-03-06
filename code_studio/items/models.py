from django.core.exceptions import ValidationError
from django.db import models
from django_resized import ResizedImageField
import datetime
from django.core.validators import FileExtensionValidator
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat



@deconstructible
class FileValidator(object):
    error_messages = {
     'max_size': ("Размер вашего изображение не должен превышать %(max_size)s."
                  " Сейчас размер вашего изображения %(size)s."),
     'min_size': ("Размер вашего изображение не должен быть меньше %(min_size)s. "
                  "Сейчас размер вашего изображения %(size)s."),
     'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, max_size=None, min_size=None, content_types=()):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size),
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                   'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.min_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'],
                                   'min_size', params)

        # if self.content_types:
        #     content_type = magic.from_buffer(data.read(), mime=True)
        #     data.seek(0)
        #
        #     if content_type not in self.content_types:
        #         params = { 'content_type': content_type }
        #         raise ValidationError(self.error_messages['content_type'],
        #                            'content_type', params)

    def __eq__(self, other):
        return (
            isinstance(other, FileValidator) and
            self.max_size == other.max_size and
            self.min_size == other.min_size and
            self.content_types == other.content_types
        )



validate_file = FileValidator(max_size=2097152)


class Item(models.Model):
    keywords_page = models.CharField('Keyword', max_length=50, default=None, blank=True)
    description_page = models.CharField('Description', max_length=50, default=None, blank=True)
    title_tag = models.CharField('title_tag', max_length=50, default=None, blank=True)
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL",)
    img = ResizedImageField(size=[1280, 1024], crop=['middle', 'center'], upload_to='media', default=None, blank=True,
                            null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'], message='Можно загрузить только формат jpeg'),
            validate_file])
    created_at = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField('Заголовок1', max_length=50, default=None)
    title2 = models.CharField('Заголовок2', max_length=50, default=None, blank=True)
    title3 = models.CharField('Заголовок3', max_length=50, default=None, blank=True)

    def __str__(self):
        return self.name


    def clean_content(self):
        content = self.cleaned_data['content']
        print(content)
        content_type = content.content_type.split('/')[0]
        print(content_type)
        # if content_type in settings.CONTENT_TYPES:
        #     if content._size > settings.MAX_UPLOAD_SIZE:
        #         raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
        #         filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        # else:
        #     raise forms.ValidationError(_('File type is not supported'))
        # return content







class Point(models.Model):
    title_num_choises = [
        ('1', 'Для первого заголовка'),
        ('2', 'Для второго заголовка'),
        ('3', 'Для третьего заголовка')
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    title_num = models.CharField(max_length=1, choices=title_num_choises)
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text
