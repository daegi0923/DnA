from rest_framework import serializers
from .models import SavingOption, SavingProduct, DepositProduct, DepositOption

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('product',)

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)


class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('product',)

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)

    