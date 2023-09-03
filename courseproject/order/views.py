from django.shortcuts import get_object_or_404, render
from order.models import OrderItem, MainOrder, WishList


def basket(request):
    context = {
        'orders': OrderItem.objects.filter(
        user=request.user,
        status=0
        ).order_by('-id')
    }
    return render(request, 'order/basket.html', context)


def checkout(request):
    main_order = MainOrder.objects.filter(user=request.user, is_done=False).first()
    return render(request, 'order/checkout.html', {'main_order': main_order})


def wish_list(request):
    wish_list = WishList.objects.filter(user=request.user).first()
    return render(request, 'product/wish_list.html', {'wish_list': wish_list})


