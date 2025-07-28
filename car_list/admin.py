from django.contrib import admin
from django.contrib.admin import register
from car_list.models import Car, Company


class CarInline(admin.TabularInline):
    model = Car


@register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'caption', 'year_created', 'color', 'image', 'create_time', 'modified_time']
    list_filter = ['company']
    search_fields = ['title', 'company', 'caption', 'year_created', 'color', 'image', 'create_time', 'modified_time']


@register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'founded_year', 'create_time', 'modified_time']
    inlines = [CarInline]