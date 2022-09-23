from django.test import TestCase

from apps.currencies.models import Currency


class CurrencyModelTestCase(TestCase):

    def test_string_representation(self):
        """Тестирование ф-ии str к объекту Currency"""
        name = 'Dollar'
        dollar = Currency(name=name, rate=66.6)
        self.assertEqual(str(dollar), name)