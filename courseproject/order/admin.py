from django.contrib import admin
from .models import MainOrder, OrderItem, WishList

admin.site.register(MainOrder)
admin.site.register(OrderItem)
admin.site.register(WishList)
