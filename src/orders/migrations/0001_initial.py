# Generated by Django 4.2.8 on 2024-01-29 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0004_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=150, verbose_name='Прізвище')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Ел. пошта')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UA', verbose_name='Номер телефону')),
                ('delivery_method', models.CharField(choices=[('NP', 'Відділення Нової пошти'), ('UP', 'Відділення Укрпошти'), ('CR', "Кур'єрська доставка"), ('SD', 'Самовивіз зі складу')], max_length=2, verbose_name='Спосіб доставки')),
                ('delivery_address', models.CharField(blank=True, max_length=400, null=True, verbose_name='Адреса доставки')),
                ('payment_method', models.CharField(choices=[('CD', 'Оплата при отриманні'), ('PP', 'Передплата на карту'), ('IP', 'Розстрочка')], max_length=2, verbose_name='Спосіб оплати')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('extra_comment', models.TextField(blank=True, null=True, verbose_name='Коментар до замовлення')),
                ('status', models.CharField(choices=[('OP', 'В обробці'), ('PP', 'Готується до відправлення'), ('', 'Прямує до замовника'), ('', 'Прибуло до відділення'), ('', 'Очікується оплата'), ('', 'Очікує на складі'), ('', 'Замовлення відмінено')], max_length=2, verbose_name='Статус замовлення')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата і час замовлення')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Акаунт покупця')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва товару')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ціна товару')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='orders.order', verbose_name='Замовлення')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods', to='goods.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Замовлений товар',
                'verbose_name_plural': 'Замовлені товари',
                'ordering': ('order',),
            },
        ),
    ]
