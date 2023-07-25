from django.urls import path
from product.views import ProductListCreateView,  CategoryListCreateView, CartListCreateView


urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('cart/', CartListCreateView.as_view()),
]