from django.db.models.signals import post_save
from django.dispatch import receiver

from finance.models import Payment


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    if instance.is_paid:
        purchase = instance.purchases.first()
        purchase.status = purchase.PAID
        purchase.save()
