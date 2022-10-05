from django.contrib import admin
from .models import Location, Region, Leisure, Image


# Register your models here.

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Region)
admin.site.register(Leisure)
