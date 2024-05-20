from rest_framework import serializers 
from django.conf import settings
from django.contrib.auth import get_user_model
from boards.serializers import BoardBreafSerializer, CommentSerializer
from products.serializers import SavingOptionSerializer, DepositOptionSerializer


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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    comment_set = CommentSerializer(many=True, read_only=True)
    board_set = BoardBreafSerializer(many=True, read_only=True)
    subscribed_deposits = DepositOptionSerializer(many=True, read_only=True, source='subscribed_deposits.all')
    subscribed_savings = SavingOptionSerializer(many=True, read_only=True, source='subscribed_savings.all')
