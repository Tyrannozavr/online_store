from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('purchases/', Purchases.as_view(), name='purchases')
]