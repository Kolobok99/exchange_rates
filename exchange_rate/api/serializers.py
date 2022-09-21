from rest_framework import serializers

from currencies.models import Currency


# class ReadOnlyModelSerializer(serializers.ModelSerializer):
#     def get_fields(self, *args, **kwargs):
#         fields = super().get_fields(*args, **kwargs)
#         for field in fields:
#             fields[field].read_only = True
#         return fields

class CurrencySerializer(serializers.ModelSerializer):
    """Сериализатор модели Currency"""

    class Meta:
        model = Currency
        fields = "__all__"
        read_only_fields = [f.name for f in Currency._meta.get_fields()]