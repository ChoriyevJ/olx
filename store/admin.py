from django.contrib import admin

from store import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", 'main_photo']


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
