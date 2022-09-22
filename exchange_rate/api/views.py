import logging

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from currencies.models import Currency
from .serializers import CurrencySerializer

logger = logging.getLogger('main')

class CurrencyAPIViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        logger.debug(f'CurrencyAPI - LIST - START')
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.debug(f'CurrencyAPI - RETRIEVE (pk={kwargs["pk"]}) - START')
        return super().retrieve(request, *args, **kwargs)