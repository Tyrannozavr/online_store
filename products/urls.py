from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='product_list'),
    path('<int:pk>/', ProductsDetail.as_view(), name='product_detail')
]