from django.test import TestCase

from apps.api.serializers import CurrencySerializer
from apps.currencies import Currency


class CurrencySerializerTestCase(TestCase):
    """Класс тестирования CurrencySerializer"""

    def setUp(self):
        self.currency_attributes = {
            'name': 'USD',
            'rate': 60.12
        }

        self.serializer_data = {
            'name': 'EURO',
            'rate': 68.12
        }

        self.currency = Currency.objects.create(**self.currency_attributes)
        self.serializer = CurrencySerializer(instance=self.currency)

    def test_contains_expected_fields(self):
        """Тест: сериализатор содержит нужные атрибуты"""
        data = self.serializer.data
        self.assertEqual(data.keys(), {'id', 'name', 'rate'})

    def test_name_field_content(self):
        """Тест: сериализатор содежрит ожидаемое значение для 'name'"""
        data = self.serializer.data
        print(data)
        self.assertEqual(data['name'], self.currency_attributes['name'])

    def test_rate_field_content(self):
        """Тест: сериализатор содежрит ожидаемое значение для 'rate'"""
        data = self.serializer.data

        self.assertEqual(data['rate'], self.currency_attributes['rate'])

    def test_creating_instance_is_forbidden(self):
        """Тест: создание записей запрещено"""

        serializer = CurrencySerializer(data=self.serializer_data)
        serializer.is_valid()
        self.assertNotEqual(0, len(self.serializer_data))
        self.assertEqual(0, len(serializer.data))

    def test_updating_instance_is_forbidden(self):
        """Тест: обновление записи возвращает туже запись"""
        instance = Currency.objects.first()
        serializer = CurrencySerializer(instance=instance, data=self.serializer_data)
        serializer.is_valid()
        serializer.save()

        self.assertEqual(serializer.data['name'], instance.name)
        self.assertEqual(serializer.data['rate'], instance.rate)