from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # {% url 'add_to_cart' product.id %}
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
]
