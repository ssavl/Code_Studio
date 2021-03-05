from custom_admin.admin import admin_site
from .models import *



admin_site.register(Item)
admin_site.register(Point)
