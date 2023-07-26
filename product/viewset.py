from product.models import Product

class ProductViewSet(viewset.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Product.category)
        return queryset

