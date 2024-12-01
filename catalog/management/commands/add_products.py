from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Product


class Command(BaseCommand):

    help = "Add testing products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
