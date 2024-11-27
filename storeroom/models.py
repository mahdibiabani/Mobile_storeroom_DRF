from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Mobile(models.Model):
    INVENTORY_STATUS_AVAILABLE = 'a'
    INVENTORY_STATUS_UNAVAILABLE = 'u'


    INVENTORY_STATUS = [
        (INVENTORY_STATUS_AVAILABLE, "Available"),
        (INVENTORY_STATUS_UNAVAILABLE, "Unavailable"),
    ]

    brand = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    model= models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    screen_size = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.01'))])
    status = models.CharField(max_length=1, choices=INVENTORY_STATUS)
    made_in = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.brand} {self.model}'
    
