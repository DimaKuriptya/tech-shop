# Generated by Django 4.2.8 on 2024-01-22 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0004_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Кількість')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True, verbose_name='Ключ сесії')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Власник')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар корзини',
                'verbose_name_plural': 'Товари корзини',
                'ordering': ('owner',),
            },
        ),
    ]
