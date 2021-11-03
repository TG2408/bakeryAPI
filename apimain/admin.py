from django.contrib import admin
from . models import IngridientQuantity, Ingridients, Products

# Register your models here.
admin.site.register(Ingridients)
admin.site.register(Products)
admin.site.register(IngridientQuantity)
