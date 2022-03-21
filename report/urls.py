from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('purchases/', Purchases.as_view(), name='purchases'),
    path('categorys/', Category_report.as_view(), name='categorys'),
    path('products/', Product_report.as_view(), name='products'),
]