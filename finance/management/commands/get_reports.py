from django.core.management import BaseCommand
from django.db.models import Sum, Count

from finance.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        payment = Payment.objects.aggregate(total=Sum('amount'), count=Count('id'))
        print(f"\n\n\nThe number of accounts are {payment['count']} and total of salary is {payment['total']} toman!\n\n\n")







