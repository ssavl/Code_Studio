from django.shortcuts import render
from .models import Item, Point
from django.core.exceptions import ObjectDoesNotExist



def product(request, id):
    try:
        keywords_page = Item.objects.latest('id').keywords_page
    except ObjectDoesNotExist:
        keywords_page = ''

    try:
        description_page = Item.objects.latest('id').description_page
    except ObjectDoesNotExist:
        description_page = ''

    try:
        title_tag = Item.objects.latest('id').title_tag
    except ObjectDoesNotExist:
        title_tag = ''
    try:
        name = Item.objects.get(id=id).name
    except ObjectDoesNotExist:
        name = 'Тут будет имя товара'
    try:
        img = Item.objects.get(id=id).img.url
    except ObjectDoesNotExist:
        img = None
    try:
        title = Item.objects.get(id=id).title
    except ObjectDoesNotExist:
        title = ''
    try:
        title2 = Item.objects.get(id=id).title2
    except ObjectDoesNotExist:
        title2 = ''
    try:
        title3 = Item.objects.get(id=id).title3
    except ObjectDoesNotExist:
        title3 = ''
    try:
        points = Point.objects.filter(item=Item.objects.get(id=id), title_num=1)
    except ObjectDoesNotExist:
        points = ''
    try:
        points2 = Point.objects.filter(item=Item.objects.get(id=id), title_num=2)
    except ObjectDoesNotExist:
        points2 = ''
    try:
        points3 = Point.objects.filter(item=Item.objects.get(id=id), title_num=3)
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


