from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    pass


# models should be registered separately
admin.site.register(Cart)
admin.site.register(CartItem)
