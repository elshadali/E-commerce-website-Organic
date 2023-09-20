from django.contrib import admin
from .models import (Product, ProductImage, Category, ProductReview)


class InlinePointAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'price', 'price_currency']
    prepopulated_fields = {"slug": ("name",)}
    inlines = (InlinePointAdmin,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ProductReview)

