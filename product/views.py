from rest_framework import generics
from .models import Category, Product, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer
from product.viewset import ProductViewSet

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFilterListView(generics.ListCreateAPIView):
    @api_view(['FILTER'])
    def get_product(request):
        if request.method in Product.category:
            queryset = ProductViewSet
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)




class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

