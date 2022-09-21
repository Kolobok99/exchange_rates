from django.db import models


class Currency(models.Model):
    """Модель Валюты"""

    name = models.CharField('название', max_length=32, unique=True)
    rate = models.FloatField('курс к рублю')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'