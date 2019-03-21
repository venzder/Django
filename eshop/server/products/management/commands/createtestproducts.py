from django.core.management.base import BaseCommand, CommandError

from products.models import Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--range', type=int, required=False, default=10)

    def handle(self, *args, **options):
        try:
            for idx in range(1, options.get('range') + 1):
                product_name = f'[test]-product-{idx}'
                Product.objects.create(
                    name=product_name
                )
                self.stdout.write(
                    self.style.SUCCESS(product_name)
                )
        except Exception as err:
            raise CommandError(err)

