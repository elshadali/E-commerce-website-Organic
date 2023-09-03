from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
from bloq.models import Bloq

def index(request):

   context = {
      'featured_products' : Product.objects.all()[:8],
      'latest_products' : Product.objects.all()[:3],
      'top_rated_products' : Product.objects.all()[:3],
      'review_products' : Product.objects.all()[:3],
      'bloqs' : Bloq.objects.all()[:3]

   }
   return render(request, 'home/index.html', context)


def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    context = {
        'result_count': len(products),
        'query': query,
        'results': products
    }

    return render(request, 'product/search.html', context)
    