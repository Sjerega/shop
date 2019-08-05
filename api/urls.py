from django.urls import path, include
from rest_framework import permissions, routers
from api.views import ProductViewSet, CategoryViewSet, TagViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
