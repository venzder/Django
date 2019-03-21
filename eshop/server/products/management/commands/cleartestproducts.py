from django.core.management.base import BaseCommand, CommandError

from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            query = Product.objects.filter(name__startswith='[test]')
            query.delete()
            self.stdout.write(
                self.style.SUCCESS('test products succesed removed')
            )
        except Exception as err:
            raise CommandError(err)
