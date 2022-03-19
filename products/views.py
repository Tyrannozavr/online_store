from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from . import models
import django.forms

class Products(ListView):
    model = models.Products

class ProductsDetail(DetailView):
    model = models.Products

    def post(self, request, *args, **kwargs):
        if request.POST:
            print('post')
            print(request.POST['count'])
            print(request.POST['discount'])
        print(args)
        print(kwargs)
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