from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect, render, reverse
from products.models import Discount

from .forms import *


def index(request):
    return render(request, 'online_store/index.html')


def register(request):
    form = Registration
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['password_again']
        email = request.POST['email']
        if not password:
            return render(request, 'registration/register.html', {'form': form, 'message': 'password can not be empty'})
        if password != password_again:
            return render(request, 'registration/register.html', {'form': form, 'message': 'passwords do not mach'})
        if not email:
            return render(request, 'registration/register.html', {'form': form, 'message': 'email not be empty'})
        if not username:
            return render(request, 'registration/register.html', {'form': form, 'message': 'username cat not be empty'})
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'registration/register.html', {'form': form})


@permission_required(perm='is_staff')
def discounts(request):
    discounts_list = Discount.objects.all()
    return render(request, 'online_store/discount_list.html', {'discounts': discounts_list})


@permission_required(perm='is_staff')
def discount_detail(request, pk):
    discount = Discount.objects.get(id=pk)
    products = discount.products_set.all()
    products = ', '.join([i.title for i in products])
    return render(request, 'online_store/discount_detail.html', {'discount': discount, 'products': products})


@permission_required(perm='is_staff')
def discount_create(request):
    if request.POST:
        name = request.POST['name']
        size = int(request.POST['size'])
        coverage = int(request.POST['coverage'])
        products = int(request.POST['products'])
        discount = Discount.objects.create(name=name, discount=size)

        if coverage:   #coverage can haves values 1 or 0, 1 mean that coverage is category, 0 that coverage is product

            try:
                category = Category.objects.get(id=products)
                discount.category = category
                discount.save()
                products = category.products_set.all()
            except ObjectDoesNotExist:
                return render(request, 'online_store/discount_create.html',
                              {'message': 'you mistake, this is does not available category'})

            for product in products:
                discounts = list(product.discount.all())
                discounts.append(discount)
                product.discount.set(discounts)

        else:
            try:
                product = Products.objects.get(id=products)
            except ObjectDoesNotExist:
                return render(request, 'online_store/discount_create.html',
                              {'message': 'you mistake, this is does not available product'})
            discounts = list(product.discount.all())
            discounts.append(discount)
            product.discount.set(discounts)

    form = CreateDiscount
    return render(request, 'online_store/discount_create.html', {'form': form})
