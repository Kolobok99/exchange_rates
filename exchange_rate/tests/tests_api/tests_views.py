from django.contrib.auth.models import User
from django.db.models import Model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.utils.serializer_helpers import ReturnDict

from currencies.models import Currency


class CurrencyAPITest(APITestCase):
    """Класс тестирования CurrencyAPIViewSet"""


    def setUp(self) -> None:

        currencies_data = [
            {'name': 'EURO', 'rate': '60.6'},
            {'name': 'DOLLAR', 'rate': '63.6'},
        ]

        for currency in currencies_data:
            Currency.objects.create(**currency)

        self.START_CURRENCY_COUNT = Currency.objects.count()

        self.test_user = User.objects.create(
           username='test_user',
           password='test_password',
           is_active=True

        )


    def test_list_currency_by_unauthorized_user(self):
        """Тест: отправка list-запроса от неваторизированного user'а"""

        url = reverse('currency-list')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


    def test_list_currency(self):
        """Тест: отправка list-запроса"""

        url = reverse('currency-list')

        self.client.force_login(user=self.test_user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.START_CURRENCY_COUNT)