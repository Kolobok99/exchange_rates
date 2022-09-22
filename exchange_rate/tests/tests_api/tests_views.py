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


class JWTAuthenticationAPITest(APITestCase):
    """Класс тестирования JWT аутентификации"""

    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_email',
            is_active=True,
        )
        self.test_user_pass = 'test_password'

        self.test_user_data = {
            'username': self.test_user.username,
            'password': self.test_user_pass,
        }

    def test_getting_token_by_valid_data(self):
        """Тест: получение jwt токена по валидным данным user'а"""

        url = reverse('token_obtain_pair')

        response = self.client.post(url, data=self.test_user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(True, 'refresh' in response.data)

    def test_getting_token_by_INvalid_data(self):
        """Тест: получение jwt токена по НЕвалидным данным user'а"""

        url = reverse('token_obtain_pair')
        user_data = {
            'username': self.test_user.username,
            'password': 'wrong_password',
        }
        error_authorization_message = 'No Active Account Found With The Given Credentials'

        response = self.client.post(url, data=user_data)
        print(response.data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertEqual(error_authorization_message, response.data['detail'].title())

    def test_update_access_token_by_valid_refresh_token(self):
        """Тест: обновление access-токена по валидному refresh-токену"""

        url = reverse('token_obtain_pair')

        response = self.client.post(url, data=self.test_user_data)
        initial_refresh_token = response.data['refresh']
        initial_access_token = response.data['access']

        url = reverse('token_refresh')
        token_data = {
            'refresh': initial_refresh_token
        }

        response = self.client.post(path=url, data=token_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(True, 'access' in response.data)
        self.assertNotEqual(initial_access_token, response.data['access'])

    def test_update_access_token_by_INvalid_refresh_token(self):
        """Тест: обновление access-токена по НЕвалидному refresh-токену"""

        url = reverse('token_obtain_pair')

        response = self.client.post(url, data=self.test_user_data)
        initial_refresh_token = response.data['refresh']
        initial_access_token = response.data['access']

        url = reverse('token_refresh')
        token_data = {
            'refresh': initial_refresh_token + 'error'
        }
        error_updating_token_message = 'Token Is Invalid Or Expired'

        response = self.client.post(path=url, data=token_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(False, 'access' in response.data)
        self.assertEqual(error_updating_token_message, response.data['detail'].title())

    def test_verify_access_token_by_valid_access_token(self):
        """Тест: верификация access-токена по валидному access-токену"""

        url = reverse('token_obtain_pair')

        response = self.client.post(url, data=self.test_user_data)
        initial_access_token = response.data['access']

        url = reverse('token_verify')
        token_data = {
            'token': initial_access_token
        }

        response = self.client.post(path=url, data=token_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, len(response.data))

    def test_verify_access_token_by_INvalid_access_token(self):
        """Тест: верификация access-токена по НЕвалидному access-токену"""

        url = reverse('token_obtain_pair')
        response = self.client.post(url, data=self.test_user_data)
        initial_access_token = response.data['access']

        url = reverse('token_verify')
        token_data = {
            'token': initial_access_token + 'error'
        }
        error_verify_token_message = 'Token Is Invalid Or Expired'

        response = self.client.post(path=url, data=token_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(error_verify_token_message, response.data['detail'].title())

    def test_verify_refresh_token_by_valid_refresh_token(self):
        """Тест: верификация refresh-токена по валидному refresh-токену"""

        url = reverse('token_obtain_pair')
        response = self.client.post(url, data=self.test_user_data)
        initial_refresh_token = response.data['refresh']

        url = reverse('token_verify')
        token_data = {
            'token': initial_refresh_token
        }

        response = self.client.post(path=url, data=token_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, len(response.data))

    def test_refresh_access_token_by_INvalid_refresh_token(self):
        """Тест: верификация refresh-токена по НЕвалидному refresh-токену"""

        url = reverse('token_obtain_pair')
        response = self.client.post(url, data=self.test_user_data)
        initial_refresh_token = response.data['refresh']

        url = reverse('token_verify')
        token_data = {
            'token': initial_refresh_token + 'error'
        }
        error_verify_token_message = 'Token Is Invalid Or Expired'

        response = self.client.post(path=url, data=token_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(error_verify_token_message, response.data['detail'].title())

