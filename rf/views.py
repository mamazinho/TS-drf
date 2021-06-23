from rest_framework import viewsets
from rf.serializers import ProductSerializer
from rf.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()