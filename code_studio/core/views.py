from django.shortcuts import render
from .models import HomePage
from items.models import Item
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email_send import email_sender
# from config import email, password
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist



def email_sender(name, to_email):
    msg = MIMEMultipart()

    message = f'Привет! {name}, это тестовая работа Степуры Савелия!'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to_email, msg.as_string())
    server.quit()


def start(request):
    if request.method == 'POST':
        email_sender(str(request.POST['name']), str(request.POST['email']))

    page_text = []

    try:
        for i in HomePage.objects.latest('id').text.split('\r\n'):
            if i ==  '':
                continue
            else:
                page_text.append(i)
    except ObjectDoesNotExist:
        pass

    try:
        keywords_page = HomePage.objects.latest('id').keywords_page
    except ObjectDoesNotExist:
        keywords_page = ''

    try:
        description_page = HomePage.objects.latest('id').description_page
    except ObjectDoesNotExist:
        description_page = ''

    try:
        title_tag = HomePage.objects.latest('id').title_tag
    except ObjectDoesNotExist:
        title_tag = ''

    try:
        title = HomePage.objects.latest('id').title
    except ObjectDoesNotExist:
        title = 'Тут будет заголовок'

    try:
        latitude = HomePage.objects.latest('id').latitude
    except ObjectDoesNotExist:
        latitude = 50

    try:
        longitude = HomePage.objects.latest('id').longitude
    except ObjectDoesNotExist:
        longitude = 60

    try:
        slider1 = HomePage.objects.latest('id').first_img.url
    except ObjectDoesNotExist:
        slider1 = None

    try:
        slider2 = HomePage.objects.latest('id').second_img.url
    except ObjectDoesNotExist:
        slider2 = None

    try:
        slider3 = HomePage.objects.latest('id').third_img.url
    except ObjectDoesNotExist:
        slider3 = None

    try:
        slider4 = HomePage.objects.latest('id').fourth_img.url
    except ObjectDoesNotExist:
        slider4 = None

    try:
        products = Item.objects.filter().order_by('-created_at')
    except ObjectDoesNotExist:
        products = ["Тут будет первый Продукт", "Тут будет второй продукт"]






    ctx = {
        'keywords_page': keywords_page,
        'description_page': description_page,
        'title_tag': title_tag,
        'title': title,
        'text_under_slider': page_text,
        'latitude': latitude,
        'longitude': longitude,
        'slider1': slider1,
        'slider2': slider2,
        'slider3': slider3,
        'slider4': slider4,
        'products': products,
    }


    return render(request, 'index.html', context=ctx)



def test(request):
    ctx = {
        'data': 'whatever'
    }
    return render(request, 'custom_page_admin.html', context=ctx)



