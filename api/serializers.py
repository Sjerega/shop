from rest_framework import serializers
from api.models import Product, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        return f'/categories/{obj.id}/'

    class Meta:
        model = Category
        fields = ('id', 'title', 'link')


class TagSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        return f'/tags/{obj.id}/'

    class Meta:
        model = Tag
        fields = ('id', 'title', 'link')


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        return f'/products/{obj.id}/'

    class Meta:
        model = Product
        fields = ('id', 'title', 'link', 'description', 'category', 'tags', 'date_mod')
