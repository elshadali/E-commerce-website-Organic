from rest_framework import serializers
from ..models import OrderItem, MainOrder, WishList


class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = MainOrder
        fields = '__all__'


class OrderIsDoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MainOrder
        fields = ('is_done',)

class AddToWishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WishList
        fields = ('product',)