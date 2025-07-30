from django.contrib.auth.models import User
from django.db import models


# _________________________________________model separator ____________________________________________


class ShippingAddress(models.Model):
    class Meta:
        verbose_name = 'ShippingAddress'
        verbose_name_plural = 'ShippingAddress'

    def __str__(self):
        return f"{self.user}"

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=32, blank=True)
    zipcode = models.CharField(max_length=16)
    address = models.TextField()
    number = models.SmallIntegerField()


# _________________________________________model separator ____________________________________________


