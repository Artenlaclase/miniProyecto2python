from django.contrib import admin

# Register your models here.

from smartphones.models import Manufacturer, Smartphone

admin.site.register(Manufacturer)
admin.site.register(Smartphone)
