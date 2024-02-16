from django.db import models
from django.contrib.auth import get_user_model

from utils import models as utils_models


class Region(utils_models.BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class District(utils_models.BaseModel):
    title = models.CharField(max_length=31)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='districts')

    def __str__(self):
        return f'{self.title} {self.region}'


class Photo(utils_models.BaseModel):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name='photos')
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ('image', 'post')

    def __str__(self):
        return f'{self.post} - {self.image}'


class Category(utils_models.BaseModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', blank=True)
    # using for filter
    # subcategories_json = models.JSONField(blank=True, null=True)
    is_subcategory = models.BooleanField(default=False)

    # fields for price
    is_price = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    is_exchange = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubCategory(utils_models.BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='subcategories')

    def __str__(self):
        return self.title


class Post(utils_models.BaseModel):
    title = models.CharField(max_length=255)
    # field for category
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                    related_name='posts', null=True, blank=True)
    # common fields
    description = models.CharField(max_length=9000)
    main_photo = models.ImageField(upload_to='images/', null=True, blank=True)

    # fields for price
    price_type = models.CharField(max_length=10, choices=utils_models.PriceTypeChoice.choices,
                                  default=utils_models.PriceTypeChoice.PRICE, blank=True, null=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    valuta_type = models.CharField(max_length=10, choices=utils_models.ValutaChoice.choices,
                                   default=utils_models.ValutaChoice.SUM, null=True, blank=True)
    is_trade = models.BooleanField(default=False, null=True, blank=True)

    # favorites
    favorites = models.ManyToManyField(get_user_model(),
                                       related_name="favorite_posts", blank=True)
    saved_searches = models.ManyToManyField(get_user_model(),
                                            related_name="saved_posts", blank=True)
    recently_viewed = models.ManyToManyField(get_user_model(),
                                             related_name="recently_posts", blank=True)

    # contact
    address = models.ForeignKey(District, on_delete=models.CASCADE,
                                related_name='posts')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=13)

    # others
    views = models.PositiveIntegerField(default=0, editable=False)
    auto_active = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



