from django.core.management.base import BaseCommand

from homework2.myapp.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        client = Client.objects.all()
        self.stdout.write(f'{client}')
