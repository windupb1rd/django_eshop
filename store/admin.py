from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    The class is used to automatically prepopulate the slug field based on category name field.
    This class must be registered: admin.site.register(ProductAdmin)
    """

    prepopulated_fields = {'slug': ('product_name', )}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', )


admin.site.register(Product, ProductAdmin)
