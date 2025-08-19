from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from basket.forms import AddToBasketForm
from car_list.models import Car, Company


def show_cars_list(request):
    # return HttpResponse("salam bar shoma! avvalin view!")
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    # return render(request, 'car_list/show_all_cars.html', context)
    return render(request, 'cover/index.html', context)


def show_car(request, car_id):
    the_car = get_object_or_404(Car, id=car_id)
    form = AddToBasketForm({'car': car_id, 'quantity': 1})
    return render(request, 'car_list/show_car.html', {'the_car': the_car, 'form': form})


