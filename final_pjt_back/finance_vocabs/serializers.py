from rest_framework import serializers
from .models import Vocas

class VocasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocas
        fields = '__all__'