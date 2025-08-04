from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from finance.utils.zarinpal import zpal_request_handler, zpal_payment_checker

from finance.forms import ChargeWalletForm


class ChargeWalletView(View):
    form_class = ChargeWalletForm
    template_name = "finance/charge_wallet.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            payment_link, authority = zpal_request_handler(
                merchant_id=settings.ZARRINPAL['merchant_id'],
                amount=form.cleaned_data['amount'],
                detail="Wallet Charge",
                user_email="mohammad@yahoo.com",
                user_phone_number=None,
                callback=settings.ZARRINPAL['gateway_callback_url'],
            )
            if payment_link is not None:
                print(authority)
                return redirect(payment_link)

        return render(request, self.template_name, {'form': form})


class VerifyView(View):
    template_name = 'callback.html'

    def get(self, request, *args, **kwargs):
        authority = request.GET.get('Authority')
        is_paid, ref_id = zpal_payment_checker(
            merchant_id=settings.ZARRINPAL['merchant_id'],
            amount=10000,
            authority=authority
        )
        return render(request, self.template_name, {'is_paid': is_paid, 'ref_if': ref_id})





