from rest_framework import serializers

from currencies.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """Сериализатор модели Currency"""

    class Meta:
        model = Currency
        fields = "__all__"
        read_only_fields = [f.name for f in Currency._meta.get_fields()]