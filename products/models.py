from django.db import models
from django.contrib.auth.models import User


class Discount(models.Model):
    name = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}: {self.discount}'

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Products(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount)

    def __str__(self):
        return self.title


class Purchases(models.Model):
    datetime = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
