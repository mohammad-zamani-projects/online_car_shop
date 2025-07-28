from django.db import models


# _________________________________________model separator ____________________________________________
from django.utils import timezone


class Company(models.Model):
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=64, name='company_name', verbose_name='COMPANY_NAME')
    founded_year = models.IntegerField(default=2025)


# _________________________________________model separator ____________________________________________


class Car(models.Model):
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.title

    BLACK = 1
    WHITE = 2
    RED = 3
    BLUE = 4
    GREEN = 5

    COLOR_TYPE_FIELD = (
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
    )

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128, verbose_name='TITLE')
    year_created = models.IntegerField(default=2025)
    color = models.PositiveSmallIntegerField(choices=COLOR_TYPE_FIELD)
    image = models.ImageField(blank=True, null=True, upload_to='car_list')
    caption = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', default=timezone.now)


# _________________________________________model separator ____________________________________________



