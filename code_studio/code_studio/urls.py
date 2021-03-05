from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from core import views
from custom_admin.admin import admin_site
from . import settings
from django.conf.urls.static import static
from django.conf.urls import url
from items.views import product


urlpatterns = [
    url(r'^admin/', admin_site.urls),
    path('admin/test', views.test),
    path('', views.start),
    path('product/<int:id>', product),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

