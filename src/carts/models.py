from django.db import models
from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        if self:
            return round(sum(cart.product_price() for cart in self), 2)
        return 0

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', blank=True, null=True, verbose_name='Власник')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, blank=True, null=True, verbose_name='Ключ сесії')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        verbose_name = 'Товар кошика'
        verbose_name_plural = 'Товари кошика'
        ordering = ('owner',)

    objects = CartQueryset().as_manager()

    def __str__(self):
        if self.owner:
            return f'{self.owner.email} wants to buy {self.quantity}x of {self.product.name}'
        return f'session key {self.session_key} wants to buy {self.quantity}x of {self.product.name}'

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
