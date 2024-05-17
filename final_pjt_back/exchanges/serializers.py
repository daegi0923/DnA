from rest_framework import serializers
from .models import ExchangeRate
from decimal import Decimal

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'

