from rest_framework import generics, permissions
from .models import Category, Product, CartItem
from .permissions import IsAuthorOrAdmin, IsAuthor
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthorOrAdmin(),)
        return (permissions.AllowAny(),)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthor(),)
        return (permissions.AllowAny(),)

class CartListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthor(),)
        return (permissions.AllowAny(),)




