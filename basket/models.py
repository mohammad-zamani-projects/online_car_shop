from django.contrib.auth.models import User
from django.db import models
from car_list.models import Car


# _________________________________________model separator ____________________________________________


class CarBasket(models.Model):
    class Meta:
        verbose_name = 'CarBasket'
        verbose_name_plural = 'CarBaskets'

    def __str__(self):
        return f"{self.user}"

    def add(self, car, qty=1):
        if self.lines.filter(cars=car).exists():
            car_line = self.lines.filter(cars=car).first()
            car_line.quantity += qty
            car_line.save()
        else:
            car_line = self.lines.create(cars=car, quantity=qty)  # CarBasketLine.objects.create(cars=car, basket=self)
        return car_line

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets', null=True, blank=True)

    def validate_user(self, user):
        if user.is_authenticated:
            if self.user is not None and self.user != user:  # if user authenticated but the basket is Not for him!!!!
                return False
            if self.user in None:
                self.user = user
                self.save()

        elif self.user is not None:
            return False
        return True

    @classmethod
    def get_basket(cls, basket_id):
        if basket_id is None:
            car_basket = cls.objects.create()
        else:
            try:
                car_basket = cls.objects.get(id=basket_id)
            except cls.DoesNotExist:
                car_basket = None
        return car_basket


# _________________________________________model separator ____________________________________________


class CarBasketLine(models.Model):
    class Meta:
        verbose_name = 'CarBasketLine'
        verbose_name_plural = 'CarBasketLines'

    def __str__(self):
        return f"{self.basket} => {self.cars} , {self.quantity}"

    basket = models.ForeignKey(CarBasket, on_delete=models.CASCADE, related_name='lines')
    cars = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='lines')
    quantity = models.PositiveSmallIntegerField(default=1)


# _________________________________________model separator ____________________________________________








