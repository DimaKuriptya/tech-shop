# Generated by Django 4.2.8 on 2024-01-09 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Товар')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Ціна зі знижкою')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='goods/', verbose_name='Фото')),
                ('storage_amount', models.PositiveIntegerField(default=0, verbose_name='Кількість на складі')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний товар')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='goods.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
