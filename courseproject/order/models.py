from django.db import models
from product.utils.options import ORDER_STATUSES


class OrderItem(models.Model):
    user = models.ForeignKey(
        'account.Account',
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    product_qty = models.PositiveIntegerField(
        default=1
    )
    status = models.IntegerField(
        choices=ORDER_STATUSES,
        default=0
    )
    order = models.ForeignKey(
        'order.MainOrder', 
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f"{self.user.email} - {self.product.name}"
    
    @property
    def get_total_price(self):
        return self.product_qty * self.product.price


class MainOrder(models.Model):
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    shipping = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(
        'account.Account',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user.email} - {self.total}"


class WishList(models.Model):
    user = models.ForeignKey(
        'account.Account',
        related_name='wish_list',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        'product.Product',
        related_name='wish_list'
    )

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish list'

    def __str__(self):
        return f"{self.user.email}"