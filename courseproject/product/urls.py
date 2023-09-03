from django.urls import path
from .views import products_by_category, product_detail, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/categories/<slug:category_slug>', products_by_category, name='products_by_category'),
    path('products/<slug:product_slug>', product_detail, name='product_detail')
]