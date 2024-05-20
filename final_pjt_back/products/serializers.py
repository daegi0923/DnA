from rest_framework import serializers
from .models import SavingOption, SavingProduct, DepositProduct, DepositOption

class SavingOptionSerializer(serializers.ModelSerializer):
    class SavingProductInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingProduct
            fields = ('id', 'fin_prdt_cd', 'fin_prdt_nm','fin_co_no','kor_co_nm',)
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('product',)
    product_info = SavingProductInfoSerializer(read_only=True, source='product')

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)


class DepositOptionSerializer(serializers.ModelSerializer):
    class DepositProductInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProduct
            fields = ('id', 'fin_prdt_cd', 'fin_prdt_nm','fin_co_no','kor_co_nm')
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('product',)
    product_info = DepositProductInfoSerializer(read_only=True, source='product')
    
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)

    