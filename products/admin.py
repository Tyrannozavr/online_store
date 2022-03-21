from django.contrib import admin
from .models import *

admin.site.register(Category)


@admin.register(Purchases)
class Purchases(admin.ModelAdmin):
    list_display = ['datetime', 'customer', 'product', 'count', 'discount']
    list_filter = ['datetime', 'discount', 'product']

@admin.register(Discount)
class AdminDiscount(admin.ModelAdmin):
    list_display = ['name', 'discount', 'category']

@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display = ['title']