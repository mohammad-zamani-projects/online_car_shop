from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from finance.models import Payment, Gateway
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
                print(payment_link)
                return redirect(payment_link)

        return render(request, self.template_name, {'form': form})


class VerifyView(View):
    template_name = 'callback.html'

    def get(self, request, *args, **kwargs):
        authority = request.GET.get('Authority')
        try:
            payment = Payment.objects.get(authority=authority)  # here, the post_init signal is calling
        except Payment.DoesNotExist:
            raise Http404
        data = dict(merchant_id=payment.gateway.auth_data, amount=payment.amount, authority=payment.authority)
        payment.verify(data)

        return render(request, self.template_name, {'payment': payment})


class PaymentView(View):

    def get(self, request, invoice_number, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        gateways = Gateway.objects.filter(is_enable=True)

        return render(request, 'finance/payment_detail.html', {'payment': payment, 'gateways': gateways})


class PaymentGatewayView(View):

    def get(self, request, invoice_number, gateway_code, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        try:
            gateway = Gateway.objects.get(gateway_code=gateway_code)
        except Gateway.DoesNotExist:
            raise Http404

        payment.gateway = gateway
        payment.save()
        payment_link = payment.bank_page
        if payment_link:
            return redirect(payment.bank_page)

        gateways = Gateway.objects.filter(is_enable=True)
        return render(request, 'finance/payment_detail.html', {'payment': payment, 'gateways': gateways})




