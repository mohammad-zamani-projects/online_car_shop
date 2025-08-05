import json
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from finance.utils import zpal_request_handler, zpal_payment_checker

class Gateway(models.Model):
    """
    Save Gateways name and credentials to the db and use them to handle payments
    """

    # CAUTION: do not change bellow function name
    FUNCTION_SAMAN = 'saman'
    FUNCTION_SHAPARAK = 'shaparak'
    FUNCTION_FINOTECH = 'finotech'
    FUNCTION_ZARRINPAL = 'zarrinpal'
    FUNCTION_PARSIAN = 'parsian'
    GATEWAY_FUNCTIONS = (
        (FUNCTION_SAMAN, _('Saman')),
        (FUNCTION_SHAPARAK, _('Shaparak')),
        (FUNCTION_FINOTECH, _('finotech')),
        (FUNCTION_ZARRINPAL, _('zarrinpal')),
        (FUNCTION_PARSIAN, _('parsian'))
    )

    title = models.CharField(max_length=100, verbose_name=_("gateway title"))
    gateway_request_url = models.CharField(max_length=150, verbose_name=_("request url"))
    gateway_verify_url = models.CharField(max_length=150, verbose_name=_("verify url"))
    gateway_code = models.CharField(max_length=12, verbose_name=_("gateway code"), choices=GATEWAY_FUNCTIONS)
    is_enable = models.BooleanField(_("is enable"), default=True)
    auth_data = models.TextField(verbose_name=_("auth_data"), null=True, blank=True)

    class Meta:
        verbose_name = _("Gateway")
        verbose_name_plural = _("Gateways")

    def __str__(self):
        return self.title

    def get_request_handler(self):
        handlers = {
            self.FUNCTION_SAMAN: None,
            self.FUNCTION_SHAPARAK: None,
            self.FUNCTION_FINOTECH: None,
            self.FUNCTION_ZARRINPAL: zpal_request_handler,
            self.FUNCTION_PARSIAN: None,
        }
        return handlers[self.gateway_code]

    def get_verify_handler(self):
        handlers = {
            self.FUNCTION_SAMAN: None,
            self.FUNCTION_SHAPARAK: None,
            self.FUNCTION_FINOTECH: None,
            self.FUNCTION_ZARRINPAL: zpal_payment_checker,
            self.FUNCTION_PARSIAN: None,
        }
        return handlers[self.gateway_code]

    @property
    def credentials(self):
        return json.loads(self.auth_data)


class Payment(models.Model):
    invoice_number = models.UUIDField(verbose_name=_('invoice number'), unique=True, default=uuid.uuid4)
    amount = models.PositiveIntegerField(verbose_name=_('payment amount'), editable=True)
    gateway = models.ForeignKey(Gateway, on_delete=models.PROTECT, null=True, blank=True, verbose_name=_('gateway'), related_name='payments')
    is_paid = models.BooleanField(verbose_name=_('is paid status'), default=False)
    payment_log = models.TextField(verbose_name=_('logs'), blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), null=True, on_delete=models.SET_NULL)
    authority = models.CharField(max_length=64, verbose_name=_('authority'), blank=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return self.invoice_number.hex

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._b_is_paid = self.is_paid

    @property
    def bank_page(self):
        handler = self.gateway.get_request_handler()
        if handler is not None:
            return handler(self.gateway, self)

    @property
    def title(self):
        return _("Instant payment")

    def status_changed(self):
        return self.is_paid != self._b_is_paid

    def verify(self, data):
        handler = self.gateway.get_verify_handler()
        if not self.is_paid and handler is not None:
            handler(self, data)
        return self.is_paid












