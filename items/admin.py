from django.contrib import admin
from . models import Item, Offer
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Item, ItemAdmin)




