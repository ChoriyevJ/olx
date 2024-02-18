from django.db import models

from utils.models import BaseModel


class PLan(BaseModel):
    title = models.CharField(max_length=255)
    plan_detail = models.ManyToManyField('PlanDetail')

    def __str__(self):
        return self.title


class PlanPrice(BaseModel):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)
    price = models.CharField(max_length=20)

    def __str__(self):
        return f'PlanPrice(pk={self.pk}, plan="{self.plan}")'


class PlanDetailGroup(BaseModel):
    title = models.CharField(max_length=255)
    is_multiple = models.BooleanField(default=False)
    text = models.TextField()

    def __str__(self):
        return self.title


class PLanDetail(BaseModel):

    class TextChoice(models.TextChoices):
        WEEK = 'WEEK', '7 kun'
        MONTH = 'MONTH', '30 kun'

    group = models.ForeignKey('PlanDetailGroup', on_delete=models.CASCADE,
                              blank=True, null=True)
    code = models.CharField(max_length=255)
    choice_text = models.CharField(max_length=255, choices=TextChoice.choices,
                                   null=True, blank=True)
    amount = models.CharField(max_length=255)

    def __str__(self):
        return f'PlanDetail(pk={self.pk}, group="{self.group}")'


class PlanDetailPrice(BaseModel):
    plan_detail = models.ForeignKey(PLanDetail, on_delete=models.CASCADE)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)
    price = models.CharField(max_length=20)

    def __str__(self):
        return f'PlanDetailPrice(pk={self.pk})'


