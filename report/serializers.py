from rest_framework import serializers
from products import models

class PurchasesSerializer(serializers.ModelSerializer):
    new_field = serializers.SerializerMethodField('name')

    def name(self, foo):
        return foo.count * 3


    product = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')

    class Meta:
        model = models.Purchases
        fields = ('count', 'product', 'new_field')

