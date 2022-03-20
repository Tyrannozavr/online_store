from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import PurchasesSerializer
from products import models

@api_view(['GET'])
def index(request):
    return Response({
        'purchases': reverse('purchases', request=request)
    })
class Purchases(ListAPIView):
    serializer_class = PurchasesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PurchasesSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Purchases.objects.raw('''
            SELECT title, products_purchases.id, (price * products_purchases.count) as price, 
             discount as size_discount, TIME(datetime) as time FROM products_purchases
            INNER JOIN products_products on  products_purchases.product_id = products_products.id
            INNER JOIN products_discount on products_purchases.discount_id = products_discount.id
            WHERE DATE(datetime)  = CURRENT_DATE;
            ''')