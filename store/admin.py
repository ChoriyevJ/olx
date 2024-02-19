from django.contrib import admin

from store import models


class DistrictInline(admin.TabularInline):
    model = models.District
    extra = 0


class CategoryInline(admin.TabularInline):
    model = models.Category
    extra = 0


class SubCategoryInline(admin.TabularInline):
    model = models.SubCategory
    extra = 0


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    inlines = [DistrictInline]
    pass


# @admin.register(models.District)
# class DistrictAdmin(admin.ModelAdmin):
#     pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, SubCategoryInline]
    list_display = ('id', 'title')


# @admin.register(models.SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.PostsRecently)
class PostsRecentlyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SavedSearches)
class SavedSearchesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
