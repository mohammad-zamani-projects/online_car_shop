from django.urls import path, register_converter, re_path
from car_list.views import show_cars_list


urlpatterns = [
    path('show/', show_cars_list)
]
