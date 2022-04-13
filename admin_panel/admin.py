from django.contrib import admin
from .models import Product, Outlet


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price', 'descriptions', 'brand', 'category', 'product_image']


@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'manager_name', 'address_latitude', 'address_longitude', 'opening_time', 'closing_time', 'outlet_image']
