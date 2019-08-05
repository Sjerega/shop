from django.urls import path, include
from rest_framework import permissions, routers
from api.views import ProductViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
