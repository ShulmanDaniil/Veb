from django.contrib import admin

from .models import Category, Product, Order, OrderItem
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    ...
