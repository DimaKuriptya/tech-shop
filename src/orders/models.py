from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
from goods.models import Product


class OrderQuerySet(models.QuerySet):
    def total_price(self):
        return sum(product.product_price for product in self)

    def total_quantity(self):
        return sum(product.quantity for product in self)


class Order(models.Model):
    delivery_methods = (
        ("NP", "Відділення Нової пошти"),
        ("UP", "Відділення Укрпошти"),
        ("CR", "Кур'єрська доставка"),
        ("SD", "Самовивіз зі складу"),
    )
    payment_methods = (
        ("CD", "Оплата при отриманні"),
        ("PP", "Передплата на карту"),
        ("IP", "Розстрочка"),
    )
    statuses = (
        ("OP", "В обробці"),
        ("PP", "Готується до відправлення"),
        ("GT", "Прямує до замовника"),
        ("AR", "Прибуло до відділення"),
        ("WP", "Очікується оплата"),
        ("WS", "Очікує на складі"),
        ("OC", "Відмінено"),
        ("DN", "Виконано"),
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="orders",
        blank=True,
        null=True,
        verbose_name="Акаунт покупця",
    )
    first_name = models.CharField(max_length=150, verbose_name="Ім'я")
    last_name = models.CharField(max_length=150, verbose_name="Прізвище")
    email = models.EmailField(blank=True, null=True, verbose_name="Ел. пошта")
    phone_number = PhoneNumberField(region="UA", verbose_name="Номер телефону")
    delivery_method = models.CharField(
        max_length=2, choices=delivery_methods, verbose_name="Спосіб доставки"
    )
    delivery_address = models.CharField(
        max_length=400, blank=True, null=True, verbose_name="Адреса доставки"
    )
    payment_method = models.CharField(
        max_length=2, choices=payment_methods, verbose_name="Спосіб оплати"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    extra_comment = models.TextField(
        blank=True, null=True, verbose_name="Коментар до замовлення"
    )
    status = models.CharField(
        max_length=2, choices=statuses, default='OP', blank=True, verbose_name="Статус замовлення"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата і час замовлення"
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення №{self.pk} | Замовник: {self.last_name} {self.first_name}"


class OrderedProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="goods", verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="goods",
        verbose_name="Товар",
    )
    name = models.CharField(max_length=150, verbose_name="Назва товару")
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Кількість")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Ціна товару"
    )

    class Meta:
        ordering = ("order",)
        verbose_name = "Замовлений товар"
        verbose_name_plural = "Замовлені товари"

    objects = OrderQuerySet().as_manager()

    def __str__(self):
        return f"Замовлення №{self.order.pk} | замовлено {self.name} в кількості {self.quantity}"

    @property
    def product_price(self):
        return round(self.price * self.quantity, 2)
