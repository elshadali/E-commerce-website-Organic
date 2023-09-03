from order.models import OrderItem, WishList
from product.models import Category
from contact.models import Contact
from about.models import SocialMedia


def header_and_footer(request):

    context = {
        'context_categories' : Category.objects.all(),
        'contact' : Contact.objects.first(),
        'social' : SocialMedia.objects.first()
    }
    
    if request.user.is_authenticated:
        context.update({
            'basket_order_count': OrderItem.objects.filter(user=request.user, status=0).count(),
            'wish_list_count': WishList.objects.filter(user=request.user).first().product.count()
            })


    return context