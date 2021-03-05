from django.contrib import admin
from django.urls import path
from core import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/test', views.test),
    path('', views.start),
    path('product', views.product),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

