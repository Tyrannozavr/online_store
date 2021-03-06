import django.forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView

from . import models
from .models import Purchases


class Products(ListView):
    model = models.Products


class ProductsDetail(LoginRequiredMixin, DetailView):
    model = models.Products

    def post(self, request, pk):
        product = self.get_object()
        if request.POST:
            datetime = timezone.now()
            count = request.POST['count']
            discount = models.Discount.objects.get(name=request.POST['discount'])
            user = request.user
            Purchases.objects.create(count=count, discount=discount, customer=user, product=product, datetime=datetime)
        return redirect('product_detail', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        class Buy(django.forms.Form):
            choice = [(i.name, str(i.discount)) for i in product.discount.all()]
            discount = django.forms.ChoiceField(choices=choice)
            count = django.forms.IntegerField(min_value=1)

        context['buy'] = Buy
        message = kwargs.get('message')
        if message:
            context['message'] = message
        return context
