from django import forms
from shipping.models import ShippingAddress
from lib.validators import min_length_validator
from django.core.exceptions import ValidationError


class ShippingAddressForm(forms.ModelForm):
    # zipcode = forms.CharField(min_length=16, max_length=16)  # kind of validator
    zipcode = forms.CharField(validators=[min_length_validator])

    class Meta:
        model = ShippingAddress
        fields = ['city', 'zipcode', 'address', 'number']  # can use this instead ==>  exclude = ['user']

    # todo: validate after jobs!
    # def clean_zipcode(self):
    #     zipcode = self.cleaned_data['zipcode']
    #     if len(zipcode) != 16:
    #         raise ValidationError("Length of value is not 16")
    #     return zipcode  # >>This line is SO IMPORTANT<<





