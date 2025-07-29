from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST

from basket.models import CarBasket
from car_list.models import Car
from django.shortcuts import render


@require_POST
def add_to_basket(request):
    # todo-1: user basket_id tooye cookie e ersali dare ya na.
    # todo-2: age basket_id nafrestade bood yeki besazim behesh assign konim.
    # todo-3: age user authenticate shode bood, user ro be basket ezafe konim.
    # todo-4: az tooye form ferestade shode car e morede nazar ro peyda konim.
    # todo-5: car e morede nazar ro be basket_line esh ezafe konim
    # todo-6: user ro be url e `next` befrestim
    response = HttpResponseRedirect(request.POST.get('next', '/'))

    car_basket_id = request.COOKIES.get('basket_id', None)
    if car_basket_id is None:
        car_basket = CarBasket.objects.create()
        response.set_cookie('basket_id', car_basket.id)
    else:
        try:
            car_basket = CarBasket.objects.get(id=car_basket_id)
        except CarBasket.DoesNotExist:
            raise Http404

    if request.user.is_authenticated:
        if car_basket.user is not None and car_basket.user != request.user:  # if user authenticated but the basket is Not for him!!!!
            raise Http404
        car_basket.user = request.user
        car_basket.save()

    car_id = request.POST.get('car_id', None)  # e.g. 3
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
    except:
        quantity = 1

    if car_id:
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            raise Http404
        else:
            car_basket.add(car, quantity)

    return response





