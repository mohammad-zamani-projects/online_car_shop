from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST

from basket.forms import AddToBasketForm
from basket.models import CarBasket


# @require_POST
# def add_to_basket(request):
#     response = HttpResponseRedirect(request.POST.get('next', '/'))
#
#     car_basket_id = request.COOKIES.get('basket_id', None)
#     if car_basket_id is None:
#         car_basket = CarBasket.objects.create()
#         response.set_cookie('basket_id', car_basket.id)
#     else:
#         try:
#             car_basket = CarBasket.objects.get(id=car_basket_id)
#         except CarBasket.DoesNotExist:
#             raise Http404
#
#     if request.user.is_authenticated:
#         if car_basket.user is not None and car_basket.user != request.user:  # if user authenticated but the basket is Not for him!!!!
#             raise Http404
#         car_basket.user = request.user
#         car_basket.save()
#
#     car_id = request.POST.get('car_id', None)  # e.g. 3
#     quantity = request.POST.get('quantity', 1)
#     try:
#         quantity = int(quantity)
#     except:
#         quantity = 1
#
#     if car_id:
#         try:
#             car = Car.objects.get(id=car_id)
#         except Car.DoesNotExist:
#             raise Http404
#         else:
#             car_basket.add(car, quantity)
#
#     return response


@require_POST
def add_to_basket(request):
    response = HttpResponseRedirect(request.POST.get('next', '/'))

    car_basket_id = request.COOKIES.get('basket_id', None)
    car_basket = CarBasket.get_basket(car_basket_id)
    if car_basket in None:
        raise Http404

    response.set_cookie('basket_id', car_basket.id)

    if not car_basket.validate_user(request.user):  # if user is not validated or it has a problem
        raise Http404

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(basket=car_basket)
    # Note:
    # form.is_valid()  ==>  if get True content
    # form.errors  ==>  if any errors exist, it is in this dictionary
    # form.cleaned_data  ==>  get data
    return response



