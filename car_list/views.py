from django.http import HttpResponse
from django.shortcuts import render
from car_list.models import Car, Company


def show_cars_list(request):
    # return HttpResponse("salam bar shoma! avvalin view!")
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'car_list/show_all_cars', context)


