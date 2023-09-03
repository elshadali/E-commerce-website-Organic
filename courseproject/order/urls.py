from django.urls import path

from .views import basket, checkout, wish_list


urlpatterns = [
    path('basket', basket, name='basket'),
    path('checkout', checkout, name='checkout'),
    path('wishlist', wish_list, name='wish_list'),
]