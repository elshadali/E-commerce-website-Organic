from django.db import models
from utils.current_request import get_current_request

from order.models import WishList
from .utils.options import CURRENCIES

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    


    
    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'


class Product(models.Model):
    name = models.CharField('ad', max_length=50)
    description = models.TextField('tesvir')
    price = models.DecimalField('qiymet', decimal_places=2, max_digits=10)
    price_currency = models.CharField(max_length=50, choices=CURRENCIES, default = 'AZN')
    category = models.ManyToManyField('product.Category', related_name='products')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mehsul'
        verbose_name_plural = 'Mehsullar'

    
    @property
    def has_added_to_wish_list(self):
        request = get_current_request()
        wl = WishList.objects.filter(user=request.user).first()
        product = Product.objects.filter(id=self.id).first()
        if wl and product:
            if product in wl.product.all():
                return True 
        return False




class ProductImage(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete = models.CASCADE,
        related_name= 'images'
        )
    image = models.ImageField('shekil', upload_to = 'products')


    def __str__(self):
        return self.image.name.split('/')[1]

    class Meta:
        verbose_name = 'Mehsul shekili'
        verbose_name_plural = 'Mehsullarin shekilleri'
   

class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    user = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
        related_name='reviews',

    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'