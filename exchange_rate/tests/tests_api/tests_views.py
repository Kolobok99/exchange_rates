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

    def test_retrieve_currency_by_unauthorized_user(self):
        """Тест: отправка retrieve-запроса от неваторизированного user'а"""

        instance = Currency.objects.first()

        url = reverse('currency-retrieve', kwargs={'pk': instance.pk})
        response = self.client.get(url)

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


    def test_retrieve_currency_with_valid_pk(self):
        """Тест: отправка retrieve-запроса c валидным PK"""

        instance = Currency.objects.first()

        url = reverse('currency-retrieve', kwargs={'pk': instance.pk})

        self.client.force_login(user=self.test_user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), ReturnDict)

        self.assertEqual(instance.id, response.data['id'])
        self.assertEqual(instance.name, response.data['name'])

        self.assertEqual(instance.rate, response.data['rate'])


    def test_retrieve_currency_with_INvalid_pk(self):
        """Тест: отправка retrieve-запроса c НЕ_валидным PK"""

        invalid_pk = 1000

        url = reverse('currency-retrieve', kwargs={'pk': invalid_pk})

        self.client.force_login(user=self.test_user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)