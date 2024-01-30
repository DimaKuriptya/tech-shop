# Generated by Django 4.2.8 on 2024-01-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('OP', 'В обробці'), ('PP', 'Готується до відправлення'), ('GT', 'Прямує до замовника'), ('AR', 'Прибуло до відділення'), ('WP', 'Очікується оплата'), ('WS', 'Очікує на складі'), ('OC', 'Замовлення відмінено')], default='OP', max_length=2, verbose_name='Статус замовлення'),
        ),
    ]
