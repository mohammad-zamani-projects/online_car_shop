from django.urls import path, register_converter, re_path
from car_list.views import test1


urlpatterns = [
    path('show/', test1)
]
