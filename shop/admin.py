from django.contrib import admin
from.models import *
# Register your models here.


class catogadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Catog,catogadmin)


class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img']
    list_editable=['price','stock','img']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Products,prodAdmin)