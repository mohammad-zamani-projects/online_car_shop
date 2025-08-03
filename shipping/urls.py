from django.contrib.auth.decorators import login_required
from django.urls import path

from shipping.views import address_list, address_create, AddressListView

urlpatterns = [
    # path('list/', address_list, name='address-list'),
    # path('list/', AddressListView.as_view(), name='address-list'),
    # path('list/', login_required(AddressListView.as_view()), name='address-list'),
    path('list/', AddressListView.as_view(), name='address-list'),
    path('create/', address_create, name='address-create')
]
