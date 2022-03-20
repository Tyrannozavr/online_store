from rest_framework import serializers
from products import models

class PurchasesSerializer(serializers.ModelSerializer):
    time = serializers.TimeField()
    size_discount = serializers.IntegerField()
    new_count = serializers.CharField(read_only=True)
    product = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    discount = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    price = serializers.IntegerField()

    class Meta:
        model = models.Purchases
        fields = ['product', 'discount', 'price', 'new_count', 'size_discount', 'time']


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    count = serializers.CharField()
    class Meta:
        model = models.Purchases
        fields = ['name', 'count']
