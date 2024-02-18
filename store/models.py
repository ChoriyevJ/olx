from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from utils.models import BaseModel
from utils.choices import PriceTypeChoice, ValutaChoice


class Region(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=31)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='districts')

    def __str__(self):
        return f'{self.title} {self.region}'


class Photo(BaseModel):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name='photos')
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ('image', 'post')

    def __str__(self):
        return f'{self.post} - {self.image}'

    def save(self, *args, **kwargs):
        if self.is_main is True:
            self.post.main_photo = self.image
            self.post.save()
        super().save(*args, **kwargs)


class Category(BaseModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', blank=True, null=True)
    options = models.ManyToManyField("option.Option", blank=True,
                                     related_name="categories")
    image = models.ImageField(upload_to='images/category/', null=True, blank=True)
    is_subcategory = models.BooleanField(default=False)

    # fields for price
    is_price = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    is_exchange = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='subcategories')
    options = models.ManyToManyField("option.Option",
                                     related_name='subcategories', blank=True)

    def __str__(self):
        return self.title


class Post(BaseModel):
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
    price_type = models.CharField(max_length=10, choices=PriceTypeChoice.choices,
                                  default=PriceTypeChoice.PRICE, blank=True, null=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    valuta_type = models.CharField(max_length=10, choices=ValutaChoice.choices,
                                   default=ValutaChoice.SUM, null=True, blank=True)
    is_trade = models.BooleanField(default=False, null=True, blank=True)

    # options
    options = models.ManyToManyField("option.Option", blank=True,
                                     through="option.PostOption")

    # favorites
    favorites = models.ManyToManyField(get_user_model(),
                                       related_name="favorite_posts", blank=True)
    saved_searches = models.ManyToManyField(get_user_model(),
                                            related_name="saved_posts", blank=True)

    # contact
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='posts', blank=True, null=True)
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


class Chat(BaseModel):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='buyyers')
    buyyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='sellers')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'buyer: {self.buyyer}, seller: {self.seller}'


class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/', validators=[
        FileExtensionValidator(['png', 'jpeg', 'pdf', 'docx', 'txt'])
    ])

    def __str__(self):
        return f'Message(pk={self.pk})'



