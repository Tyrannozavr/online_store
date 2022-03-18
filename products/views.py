from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from . import models
from . import forms

class Products(ListView):
    model = models.Products

class ProductsDetail(DetailView):
    model = models.Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = self.get_object()
        product = models.Products.objects.get(id=a.id)
        # print(choice.discount.all())
        form = forms.AllowDiscount
        # print([i for i in product.discount.all()])
        # print([(i.name, str(i.discount)) for i in product.discount.all()])
        form.choices = [(i.name, str(i.discount)) for i in product.discount.all()]
        # choices = [(i.name, str(i.discount)) for i in choice.discount.all()]
        # print(choices)
        # form.choices = choices
        context['discount'] = form
        print(context['discount'].choices)
        return context