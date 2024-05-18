from rest_framework import serializers 
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username')
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username
        }
