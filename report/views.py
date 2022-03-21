from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import *
from products import models

@api_view(['GET'])
def index(request):
    return Response({
        'daily report': reverse('purchases', request=request),
        'categorys report': reverse('categorys', request=request),
        'products report': reverse('products', request=request),
    })
class Purchases(ListAPIView):
    serializer_class = PurchasesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Purchases.objects.raw('''
            SELECT title, products_purchases.id, (price * products_purchases.count) as price, 
             discount as size_discount, TIME(datetime) as time FROM products_purchases
            INNER JOIN products_products on  products_purchases.product_id = products_products.id
            INNER JOIN products_discount on products_purchases.discount_id = products_discount.id
            WHERE DATE(datetime)  = CURRENT_DATE;
            ''')


class Category_report(ListAPIView):
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializers = self.serializer_class(queryset, many=True)
        return Response(serializers.data)

    def get_queryset(self):
        return models.Purchases.objects.raw('''
        SELECT products_purchases.id, products_category.title AS category, pd.name AS discount_name,
               sum(count)/ (count(DISTINCT DATE(datetime))+0.0) AS average FROM products_purchases
        JOIN products_products on products_purchases.product_id = products_products.id
        JOIN products_category on products_products.category_id = products_category.id
        JOIN products_discount pd on products_purchases.discount_id = pd.id
        WHERE pd.category_id OR pd.name = 'default'
        GROUP BY category, pd.name;
        ''')

class Product_report(ListAPIView):
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializers = self.serializer_class(queryset, many=True)
        return Response(serializers.data)

    def get_queryset(self):
        return models.Purchases.objects.raw('''
            SELECT products_purchases.id, products_products.id AS product_id, pd.name,
                sum(count)/ (count(DISTINCT DATE(datetime))+0.0) AS average FROM products_purchases
            JOIN products_products on products_purchases.product_id = products_products.id
            JOIN products_category on products_products.category_id = products_category.id
            JOIN products_discount pd on products_purchases.discount_id = pd.id
            WHERE pd.category_id is null OR pd.name = 'default'
            GROUP BY product_id, pd.name;
        ''')

