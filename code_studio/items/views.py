from django.shortcuts import render
from .models import Item, Point
from django.core.exceptions import ObjectDoesNotExist



def product(request, slug_item):
    try:
        keywords_page = Item.objects.latest('slug').keywords_page
    except ObjectDoesNotExist:
        keywords_page = ''

    try:
        description_page = Item.objects.latest('slug').description_page
    except ObjectDoesNotExist:
        description_page = ''

    try:
        title_tag = Item.objects.latest('slug').title_tag
    except ObjectDoesNotExist:
        title_tag = ''
    try:
        name = Item.objects.get(slug=slug_item).name
    except ObjectDoesNotExist:
        name = 'Тут будет имя товара'
    try:
        img = Item.objects.get(slug=slug_item)
    except ObjectDoesNotExist:
        img = None
    try:
        title = Item.objects.get(slug=slug_item).title
    except ObjectDoesNotExist:
        title = ''
    try:
        title2 = Item.objects.get(slug=slug_item).title2
    except ObjectDoesNotExist:
        title2 = ''
    try:
        title3 = Item.objects.get(slug=slug_item).title3
    except ObjectDoesNotExist:
        title3 = ''
    try:
        points = Point.objects.filter(item=Item.objects.get(slug=slug_item), title_num=1)
    except ObjectDoesNotExist:
        points = ''
    try:
        points2 = Point.objects.filter(item=Item.objects.get(slug=slug_item), title_num=2)
    except ObjectDoesNotExist:
        points2 = ''
    try:
        points3 = Point.objects.filter(item=Item.objects.get(slug=slug_item), title_num=3)
    except ObjectDoesNotExist:
        points3 = ''




    ctx = {
        'keywords_page': keywords_page,
        'description_page': description_page,
        'title_tag': title_tag,
        'name': name,
        'img': img,
        'title': title,
        'title2': title2,
        'title3': title3,
        'points': points,
        'points2': points2,
        'points3': points3,

    }

    return render(request, 'product.html', context=ctx)


