from django.core.management import BaseCommand

from apps.currencies.models import Currency
from services.logger_services import logger_wraps
from services.services import get_exchange_rates_from_cbr_ru
from core.settings import logger


class Command(BaseCommand):
    help = 'Обновление/Добавление Currency.rate'

    @logger.catch()
    @logger_wraps()
    def handle(self, *args, **options):
        """Получает список валют и создает/обновляет currency.rate"""

        valutes = get_exchange_rates_from_cbr_ru()
        for valute in valutes:
            Currency.objects.update_or_create(
                name=valute[0],
                rate=valute[1],
                defaults={'name': valute[0]})

