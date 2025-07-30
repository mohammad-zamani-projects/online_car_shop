from django import forms

from car_list.models import Car


class AddToBasketForm(forms.Form):
    car = forms.ModelChoiceField(Car.objects.all(), widget=forms.HiddenInput)  # default is: widget=forms.Select
    quantity = forms.IntegerField()

    def save(self, basket):
        basket.add(
            car=self.cleaned_data.get('car'),
            qty=self.cleaned_data.get('quantity')
        )
        return basket



