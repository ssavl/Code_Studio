from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from core import views
# from custom_admin.admin import admin_site
from . import settings
from django.conf.urls.static import static
from django.conf.urls import url
from items.views import product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start),
    path('product/<slug:slug_item>', product),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

