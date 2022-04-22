from django.http import HttpResponse
from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from store.models import Product


def _cart_id(request):

    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()

    return cart_id


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id) # get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()

    return redirect('cart')
    # return HttpResponse(cart_item.quantity)


def cart(request):

    current_cart = Cart.objects.get(cart_id=_cart_id(request))
    products_in_cart = CartItem.objects.filter(cart=current_cart.id)

    context = {
        'products': products_in_cart
    }

    return render(request, 'store/cart.html', context)
