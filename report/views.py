from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PurchasesSerializer
from rest_framework.permissions import AllowAny
from products import models

@api_view(['GET'])
def index(request):
    return Response({
        'purchases': reverse('purchases', request=request)
    })
from django.db.models import Count, Sum
class Purchases(ListAPIView):
    serializer_class = PurchasesSerializer
    # queryset = models.Purchases.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PurchasesSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        prod = models.Purchases

        # return prod.objects.aggregate(Count('id'))
        # return models.Purchases.objects.all().aggregate(Sum('count')) #.annotate(new_count=Sum('count')).order_by('new_count')


        # return models.Purchases.objects.raw('SELECT id, DISTINCT "product" FROM products_purchases')
        return models.Purchases.objects.raw('''
            SELECT title, products_purchases.id, (price * products_purchases.count) as price, 
             discount as size_discount FROM products_purchases
            INNER JOIN products_products on  products_purchases.product_id = products_products.id
            INNER JOIN products_discount on products_purchases.discount_id = products_discount.id;
            ''')

'''Время покупки
Товар
Цена
Скидка (если была)
Процент скидки (если была скидка)
'''