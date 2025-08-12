from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.update(is_active=True)
        print("\n\nAll the users are Activated...\n\n")





