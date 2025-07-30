from django import forms

from shipping.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['city', 'zipcode', 'address', 'number']  # can use this instead ==>  exclude = ['user']








