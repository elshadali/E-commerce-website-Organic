from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .forms import ReviewForm
from .models import Category, Product, ProductReview
from .utils.options import *


def products_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category,
    }
    return render(request, 'product/products_by_category.html', context)


def products_list(request):
    products = Product.objects.all()[:10]
    context = {
        'products': products,
    }
    return render(request, 'product/product_list.html', context)

class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    cat_ids = [obj.id for obj in product.category.all()]
    reviews = ProductReview.objects.filter(product=product).order_by('-created_at')
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'good')
            return redirect(reverse("product_detail", args=(product.slug,)))
        
    context = {
        'product': product,
        'related_products': Product.objects.filter(category__in=cat_ids).distinct()[:8],
        'form' : form,
        'reviews' : reviews
    }
    return render(request, 'product/detail.html', context)