from django.db import models
from django.contrib.auth import get_user_model

from olx.utils import models as utils_models


class Photo(utils_models.BaseModel):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name='photos')

    class Meta:
        unique_together = ('image', 'post')

    def __str__(self):
        return f'{self.post} - {self.image}'


class Category(utils_models.BaseModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children')
    # using for filter
    subcategories = models.JSONField(blank=True, null=True)

    # other
    is_price = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    is_exchange = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubCategory(utils_models.BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(utils_models.BaseModel):

    title = models.CharField(max_length=255)
    # field for category
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                    related_name='posts', null=True, blank=True)

    description = models.CharField(max_length=9000)

    # fields for price
    price_type = models.CharField(max_length=10, choices=utils_models.PriceTypeChoice,
                                  default=utils_models.PriceTypeChoice.PRICE)
    price = models.DecimalField(max_digits=10, null=True, blank=True)
    valuta_type = models.CharField(max_length=10, choices=utils_models.ValutaChoice.choices,
                                   default=utils_models.ValutaChoice.SUM, null=True, blank=True)
    is_trade = models.BooleanField(default=False, null=True, blank=True)

    # fields for favorites
    favorites = models.ManyToManyField(get_user_model(),
                                       related_name="favorite_posts")
    saved_searches = models.ManyToManyField(get_user_model(),
                                            related_name="saved_posts")
    recently_viewed = models.ManyToManyField(get_user_model(),
                                             related_name="recently_posts")

    # others
    views = models.PositiveIntegerField(default=0, editable=False)
    auto_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class OptionType(models.TextChoices):
    SINGLE = "SINGLE", "Single"
    EXTENDED = "EXTENDED", "Extended"
    CHOICE = "CHOICE", "Choice"
    BUTTON = "BUTTON", "Button"
    TEXT = "TEXT", "Text"
    NUMBER = "NUMBER", "Number"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE", "Multiple choice"


class Option(utils_models.BaseModel):
    post = models.ManyToManyField(Post,
                                  related_name='options')
    title = models.CharField(max_length=255)
    typ = models.CharField(max_length=15, choices=OptionType.choices)
    code = models.CharField(max_length=31, blank=True, null=True)

    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OptionValue(utils_models.BaseModel):
    option = models.ForeignKey(Option, on_delete=models.CASCADE,
                               related_name='values')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class OptionValueExtended(utils_models.BaseModel):
    option_value = models.ForeignKey(OptionValue, on_delete=models.CASCADE,
                                     related_name='extendeds', blank=True, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



