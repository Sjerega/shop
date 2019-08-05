from rest_framework.viewsets import ModelViewSet
from api.models import Product, Category, Tag
from api.serializers import ProductSerializer, CategorySerializer, TagSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = ()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = ()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = ()
    serializer_class = TagSerializer
