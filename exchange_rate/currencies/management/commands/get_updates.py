from django.core.management import BaseCommand

from currencies.models import Currency
from services.services import get_exchange_rates_from_cbr_ru


# from tests_currencies.models import Currency
# from services.services import get_exchange_rates_from_cbr_ru


class Command(BaseCommand):
    help = 'Обновление/Добавление Currency.rate'

    def handle(self, *args, **options):
        valutes = get_exchange_rates_from_cbr_ru()

        for valute in valutes:
            Currency.objects.update_or_create(
                name=valute[0],
                rate=valute[1],
                defaults={'name': valute[0]})