from rest_framework import serializers 
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'target_savings','annual_income',
                  'primary_bank')
        read_only_fields = ('subscribed_deposits' ,'subscribed_savings')