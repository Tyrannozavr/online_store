from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from . import models
import django.forms
from .models import Purchases
from datetime import datetime as dt

class Products(ListView):
    model = models.Products


class ProductsDetail(DetailView):
    model = models.Products

    def post(self, request, pk):
        product = self.get_object()
        if request.POST:
            # datetime = time.time()
            from django.utils import timezone
            now = timezone.now()
            # today = timezone.now().date()
            # print(now, today)
            # datetime = dt.now()
            datetime = now
            print(datetime)
            # print('post')
            # print(request.POST['count'])
            count = request.POST['count']
            discount = request.POST['discount']
            discount = models.Discount.objects.get(name=discount)
            user = request.user
            print(discount, type(discount))
            # print(request.POST['discount'])
            # print(pk)
            # print(request.user)
            Purchases.objects.create(count=count, discount=discount, customer=user, product=product, datetime=datetime)
        return HttpResponse('pass')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        class Buy(django.forms.Form):
            choice = [(i.name, str(i.discount)) for i in product.discount.all()]
            discount = django.forms.ChoiceField(choices=choice)
            count = django.forms.IntegerField(min_value=1)
        context['buy'] = Buy
        return context