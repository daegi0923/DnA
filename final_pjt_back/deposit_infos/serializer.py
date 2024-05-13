from rest_framework import serializers
from .models import SavingProductOptions, SavingProducts

class SavingProductsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        infos = [SavingProducts(**item) for item in validated_data]
        return SavingProducts.objects.bulk_create(infos)

class SavingProductOptionsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        options = []
        for item in validated_data:
            option = SavingProductOptions(**item)
            print(option)
            option.product = SavingProducts.objects.get(fin_prdt_cd = item.get('fin_prdt_cd'))
            options.append(option)
        return SavingProductOptions.objects.bulk_create(options)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        list_serializer_class = SavingProductsListSerializer


class SavingProductOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductOptions
        fields = '__all__'
        read_only_fields = ('product',)
        list_serializer_class = SavingProductOptionsListSerializer
        
class TopRateOptionsSerializer(serializers.Serializer):
    deposit_product = SavingProductsSerializer
    options = SavingProductOptionsSerializer
    