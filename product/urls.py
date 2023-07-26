from django.urls import path
from product.views import ProductListCreateView,  CategoryListCreateView, CartItemListCreateView, ProductFilterListView
from likes.views import LikesProductView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('cart/', CartItemListCreateView.as_view()),
    path('filter/', ProductFilterListView.as_view()),
]