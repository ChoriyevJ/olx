from django.db import models

from utils import models as utils_models


class Option(utils_models.BaseModel):
    post = models.ManyToManyField("store.Post", blank=True,
                                  through="PostOption")
    category = models.ManyToManyField("store.Category", blank=True,
                                      through="CategoryOption")
    subcategory = models.ManyToManyField("store.SubCategory",
                                         related_name='options', blank=True)
    title = models.CharField(max_length=255)
    typ = models.CharField(max_length=15, choices=utils_models.OptionType.choices)
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


class CategoryOption(utils_models.BaseModel):
    category = models.ForeignKey("store.Category", on_delete=models.CASCADE,
                                 related_name="options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE,
                               related_name="categories")

    def __str__(self):
        return f'{self.category}__{self.option}'


class PostOption(utils_models.BaseModel):
    post = models.ForeignKey("store.Post", on_delete=models.CASCADE,
                             related_name="options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE,
                               related_name="posts")

    def __str__(self):
        return f"{self.post}__{self.option}"

# class OptionValueExtended(utils_models.BaseModel):
#     option_value = models.ForeignKey(OptionValue, on_delete=models.CASCADE,
#                                      related_name='extendeds', blank=True, null=True)
#     title = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
