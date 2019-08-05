from rest_framework.viewsets import ModelViewSet
from api.models import Product, Category, Tag
from api.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = ()
    serializer_class = ProductSerializer
