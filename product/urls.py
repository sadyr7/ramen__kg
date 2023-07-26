from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductAPIView,  CategoryAPIView, CartListAPIView

router = DefaultRouter()
router.register('cart', CartListAPIView)
router.register('product', ProductAPIView)
router.register('category', CategoryAPIView)


urlpatterns = [
    path('', include(router.urls)),
]
