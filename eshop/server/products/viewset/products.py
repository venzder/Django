from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    # queryset = Product.objects.all()

    def get_queryset(self):

        queryset = Product.objects.all()
        ids = self.request.query_params.get('id__in', None)
        if ids is not None:
            ids = [int(x) for x in ids.split(',')]
            queryset = queryset.filter(id__in=ids)
        return queryset
