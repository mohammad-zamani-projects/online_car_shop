from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from finance.models import Payment


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    if instance.is_paid and not instance._b_is_paid:
        # print('Purchase signal fired!!!')
        if instance.purchase.exists():  # a signal for purchase model!
            purchase = instance.purchases.first()
            purchase.status = purchase.PAID
            purchase.save()


@receiver(post_init, sender=Payment)
def store_is_paid_status(sender, instance, **kwargs):
    # print('post_init signal calls!!!')
    instance._b_is_paid = instance.is_paid




