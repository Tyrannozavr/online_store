from rest_framework import serializers
from products import models

class PurchasesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Purchases
        fields = '__all__'

