from django.shortcuts import render
from .models import *



def start(request):
    if request.method == 'POST':
        # if form.is_valid:
        print('У нас POST запрос')
        print(request.POST['name'])
        print(request.POST['email'])

    page_text = []

    if HomePage.objects.latest('id').text:
        for i in HomePage.objects.latest('id').text.split('\r\n'):
            if i ==  '':
                continue
            else:
                page_text.append(i)

    if HomePage.objects.latest('id').title and HomePage.objects.latest('id').latitude and \
            HomePage.objects.latest('id').longitude and HomePage.objects.latest('id').first_img.url and \
            HomePage.objects.latest('id').second_img.url and HomePage.objects.latest('id').third_img.url and \
            HomePage.objects.latest('id').fourth_img.url:
        ctx = {
            'title': HomePage.objects.latest('id').title,
            'text_under_slider': page_text,
            'latitude': HomePage.objects.latest('id').latitude,
            'longitude': HomePage.objects.latest('id').longitude,
            'slider1': HomePage.objects.latest('id').first_img.url,
            'slider2': HomePage.objects.latest('id').second_img.url,
            'slider3': HomePage.objects.latest('id').third_img.url,
            'slider4': HomePage.objects.latest('id').fourth_img.url,
            'product_1': "Супер продукт",
            'product_2': "Афигенный продукт",
            'product_3': "Просто класс продукт",
            'product_4': "Надо брать продукт",
            'product_5': "Вот это да! продукт",
        }
    else:
        ctx = {}

    return render(request, 'index.html', context=ctx)



def product(request, id):
    ctx = {
        # 'title': HomePageTitle.objects.latest('id'),
        # 'text_under_slider': TextUnderSlider.objects.latest('id'),
        # 'coords': Coord.objects.latest('id'),
    }
    return render(request, 'product.html', context=ctx)


# Coord.objects.latest('id'),