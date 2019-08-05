from rest_framework import serializers
from api.models import Product, Category, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'tags')
