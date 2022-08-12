from django.conf import settings
from django.db import models


class Address(models.Model):
    "Generated Model"
    street = models.BigIntegerField()
