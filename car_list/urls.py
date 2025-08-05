from django.urls import path, register_converter, re_path
from django.views.generic import TemplateView

from car_list.views import show_cars_list, show_car


urlpatterns = [
    path('show/', show_cars_list),
    path('show/<int:car_id>', show_car, name='car-show')
]
