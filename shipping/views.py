from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import ListView, FormView

from shipping.forms import ShippingAddressForm
from shipping.models import ShippingAddress


# # @login_required(login_url='/admin/login/')
# @login_required()
# @require_GET
# def address_list(request):
#     queryset = ShippingAddress.objects.filter(user=request.user)
#     return render(request, 'shipping/list.html', {'queryset': queryset})


# class AddressListView(View):
#
#     @method_decorator(login_required)
#     def get(self, request):
#         queryset = ShippingAddress.objects.filter(user=request.user)
#         return render(request, 'shipping/list.html', {'queryset': queryset})


############################################################################################################
# todo: Inheritance in class view...!
# class CustomAddressListView(ListView):
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_queryset(self):
#         qs =super().get_queryset()
#         return qs.filter(user=self.request.user)
#
#
# class AddressListView(CustomAddressListView):
#     model = ShippingAddress
#     template_name = 'shipping/list.html'  # if dont write it, you have to rename list.html to shippingaddress_list.html
#     context_object_name = 'queryset'  # if dont write it, the value in the html file is 'object_list'
#
#     def get_context_data(self, *args, object_list=None, **kwargs):
#         context = super().get_context_data(*args, object_list=object_list, **kwargs)
#         context['extra_data'] = self.queryset().count()
#         return context
############################################################################################################


class AddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping/list.html'  # if dont write it, you have to rename list.html to shippingaddress_list.html
    context_object_name = 'queryset'  # if dont write it, the value in the html file is 'object_list'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs =super().get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_count'] = context['queryset'].count()
        return context


# # @login_required(login_url='/admin/login/')
# @login_required()
# @require_http_methods(request_method_list=['GET', 'POST'])
# def address_create(request):
#
#     if request.method == "POST":
#         form = ShippingAddressForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('address-list')
#
#     else:  # if request.method == "GET":
#         form = ShippingAddressForm()
#
#     return render(request, 'shipping/create.html', {'form': form})


# We write this part instead def address_create(request):
class AddressCreateView(FormView):
    form_class = ShippingAddressForm
    template_name = 'shipping/create.html'
    success_url = reverse_lazy('address-list')  # success_url = '/shipping/list/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):  # we over-write form_valid, because when the form is valid it doesn't save the form and just redirect us to the url path!
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)




