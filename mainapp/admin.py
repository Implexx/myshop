from django.contrib import admin
from .models import Team, Product, Image, Review, BrandLogo


# Register your models here.
admin.site.register(Team)
admin.site.register(Review)
admin.site.register(BrandLogo)


class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]

