from django.db import models

from utils.models import BaseModel
from utils.choices import OptionType


class Option(BaseModel):
    title = models.CharField(max_length=255)
    typ = models.CharField(max_length=15, choices=OptionType.choices)
    code = models.CharField(max_length=31, blank=True, null=True)
    place_holder = models.CharField(max_length=255, blank=True, null=True)
    regex = models.CharField(max_length=255, blank=True, null=True)

    order = models.PositiveSmallIntegerField(default=0)
    limit = models.IntegerField(blank=True, null=True)

    is_required = models.BooleanField(default=False)
    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OptionValue(BaseModel):
    option = models.ForeignKey(Option, on_delete=models.CASCADE,
                               related_name='values')
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class PostOption(BaseModel):
    post = models.ForeignKey("store.Post", on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.post}__{self.option}"


class PostOptionValue(BaseModel):
    post_option = models.ForeignKey(PostOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


