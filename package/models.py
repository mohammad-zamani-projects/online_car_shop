from django.db import models
from django.utils.translation import gettext


class Package(models.Model):
    title = models.CharField(max_length=48, verbose_name=gettext('title'))
    price = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    days = models.PositiveSmallIntegerField()
    is_enable = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = gettext('Package')
        verbose_name_plural = gettext('Packages')

    def __str__(self):
        return self.title


class PackageAttribute(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='attributes')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



