from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class ExtraDescriptionChoice(models.TextChoices):
#     BUSINESS = 'BUSINESS', 'Business'
#     PRIVATE = 'PRIVATE', 'Private person'


class ValutaChoice(models.TextChoices):
    SUM = 'SUM', 'Sum'
    EURO = 'EURO', 'y.e'


class PriceTypeChoice(models.TextChoices):
    PRICE = 'PRICE', 'Price'
    FREE = 'FREE', 'Free'
    EXCHANGE = 'EXCHANGE', 'Exchange'


class OptionType(models.TextChoices):
    SINGLE = "SINGLE", "Single"
    CHOICE = "CHOICE", "Choice"
    BUTTON = "BUTTON", "Button"
    TEXT = "TEXT", "Text"
    NUMBER = "NUMBER", "Number"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE", "Multiple choice"



