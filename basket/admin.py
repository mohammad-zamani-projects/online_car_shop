from django.contrib import admin
from django.contrib.admin import register
from basket.models import CarBasket, CarBasketLine


class CarBasketLineInline(admin.TabularInline):
    model = CarBasketLine


@register(CarBasket)
class CarBasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_time', 'modified_time']
    list_filter = ['user']
    inlines = [CarBasketLineInline]


# @register(CarBasketLine)
# class CarBasketLineAdmin(admin.ModelAdmin):
#     list_display = ['basket', 'cars', 'quantity']














