from django.core.management.base import BaseCommand
from centralbookings.models import Organizer

class Command(BaseCommand):
    help = 'Reset organizer numbers to None'

    def handle(self, *args, **kwargs):
        Organizer.objects.filter(Organizer_Number='TU90O').update(Organizer_Number=None)
        self.stdout.write(self.style.SUCCESS('Successfully reset organizer numbers'))