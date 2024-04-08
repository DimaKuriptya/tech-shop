from rest_framework import serializers
from goods.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'price',
            'discount_price',
            'storage_quantity',
            'is_active',
        )
