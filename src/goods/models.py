from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=100, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name="Назва")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(verbose_name="Опис")
    category_id = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
        verbose_name="Категорія",
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    discount_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Ціна зі знижкою",
    )
    photo = models.ImageField(
        upload_to="goods", blank=True, null=True, verbose_name="Фото"
    )
    storage_amount = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")
    is_active = models.BooleanField(default=True, verbose_name="Активний товар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self) -> str:
        return self.name

    def get_id(self):
        return str(self.pk).zfill(5)
