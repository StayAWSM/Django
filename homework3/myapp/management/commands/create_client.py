from django.core.management.base import BaseCommand

from homework2.myapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name=f'GigaChad',
            email=f'superpro@mail.ru',
            number_phone=f'+(1)23456789',
            address=f'Moscow'
        )
        client.save()
        self.stdout.write(f'{client}')
