from django.shortcuts import render, get_object_or_404

from category.models import Category
from .models import Product


def store(request, category_slug=None):

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)

    else:
        products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'store/product_detail.html', context)
