from django.contrib import admin

from option import models


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OptionValue)
class OptionValueAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostOption)
class PostOptionAdmin(admin.ModelAdmin):
    pass



