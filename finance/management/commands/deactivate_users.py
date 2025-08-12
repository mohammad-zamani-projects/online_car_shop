from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='*', type=str)
        parser.add_argument('--isstaff', action='store_true', help='Not deactivate staff users')
        parser.add_argument('--all', action='store_true', help='Deactivate all users')

    def handle(self, *args, **options):

        if not options['all'] and not options['username']:
            raise Exception("\vYou have to use one of '--all' or 'username' at least!\n")

        elif options['all'] and options['username']:
            raise Exception("\vPlease just use one of the '--all' or 'username' options!\n")

        if len(options['username']) == 1:
            raise Exception("\vYou have to enter one user at least\n")

        usernames = options['username']

        if options['username']:
            users = User.objects.filter(username__in=usernames)
            if options['isstaff']:
                users.filter(is_staff=False)
            if users.exists():
                users.update(is_active=False)
                print(f"\n\nThe user {users.get()} is Deactivated...\n\n")

        elif options['all']:
            # users = User.objects.filter(is_staff=False) if options['issstaff'] else User.objects.all()
            users = User.objects.all() if not options['isstaff'] else User.objects.filter(is_staff=False)
            users.update(is_active=False)
            print("\n\nAll the users are Deactivated\n")







