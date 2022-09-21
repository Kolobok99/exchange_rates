from rest_framework.serializers import ModelSerializer

from currencies.models import Currency


class CurrencySerializer(ModelSerializer):
    """Сериализатор модели Currency"""

    class Meta:
        model = Currency
        fields = "__all__"