from django.urls import path
from product.views import ProductListCreateView,  CategoryListCreateView, CartItemListCreateView


urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('cart/', CartItemListCreateView.as_view()),
]