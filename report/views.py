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

class Purchases(ListAPIView):
    serializer_class = PurchasesSerializer
    queryset = models.Purchases.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # queryset = models.Purchases.objects.raw('SELECT "products_purchases"."id", "datetime" FROM products_purchases;')
        serializer = PurchasesSerializer(queryset, many=True)
        # serializer = self.get_serializer()(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Purchases.objects.all()
        # return models.Purchases.objects.raw('\
        #     SELECT "id", "products_purchases"."id" * 2 AS ADDED FROM products_purchases;\
        # ')

'''Время покупки
Товар
Цена
Скидка (если была)
Процент скидки (если была скидка)
'''

