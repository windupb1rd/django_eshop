from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    The class is used to automatically prepopulate the slug field based on category name field.
    This class must be registered: admin.site.register(CategoryAdmin)
    """

    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('category_name', 'slug', )


admin.site.register(Category, CategoryAdmin)
