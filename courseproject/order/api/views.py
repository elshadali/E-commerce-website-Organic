from django.urls import reverse
from product.models import Product
from rest_framework import generics
from rest_framework.response import Response
import json
from .serializers import AddToWishListSerializer, OrderIsDoneSerializer, OrderItemSerializer, OrderSerializer
from ..models import OrderItem, MainOrder, WishList

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'

class MainOrderCreateAPIView(generics.CreateAPIView):
    queryset = MainOrder.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        data = serializer.data
        data['absolute_url'] = request.build_absolute_uri(reverse("checkout"))
        MainOrder.objects.filter(user=request.user, is_done=False).exclude(id=instance.id).delete()
        if items:= json.loads(request.data.get('items', '[]')):
            for item in items:
                if item is not None:
                    obj = OrderItem.objects.get(
                        id=int(item),
                    )
                    instance.items.add(obj)

        return Response({"detail": "OK", 'data': data}, status=201)

class OrderIsDoneAPIView(generics.UpdateAPIView):
    queryset = MainOrder.objects.all()
    serializer_class = OrderIsDoneSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        order_id = self.kwargs.get('id', None) 
        main_order = MainOrder.objects.get(id=order_id)
        main_order.is_done = True
        print('main_order', main_order)
        order_items = OrderItem.objects.filter(order=main_order)
        order_items.update(status=2)
        print('order_items', order_items)
        print('order_items_statuses', [item.status for item in order_items])
        return super().put(request, *args, **kwargs)
    



class AddToWishListAPIView(generics.GenericAPIView):
    queryset = WishList.objects.all()
    serializer_class = AddToWishListSerializer

    def put(self, request, *args, **kwargs):
        wishlist_id = self.kwargs.get('id', None) 
        try:
            wish_list = WishList.objects.get(user=request.user)
        except Exception as e:
            wish_list = WishList.objects.create(user=request.user)    

        product_id = int(request.data.get('product'))
        added_product = Product.objects.get(id=product_id)

        wish_list.product.add(added_product)
        return Response({"detail": "OK"}, status=200)


class RemoveFromWishListAPIView(generics.GenericAPIView):
    queryset = WishList.objects.all()
    serializer_class = AddToWishListSerializer

    def put(self, request, *args, **kwargs):
        wishlist_id = self.kwargs.get('id', None) 
        try:
            wish_list = WishList.objects.get(user=request.user)
        except Exception as e:
            wish_list = WishList.objects.create(user=request.user)    

        product_id = int(request.data.get('product'))
        added_product = Product.objects.get(id=product_id)

        wish_list.product.remove(added_product)
        return Response({"detail": "OK"}, status=200)