from rest_framework import serializers 
from .models import Board, Comment
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

class BoardBreafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('board', 'created_at')
    user = UserSerializer(read_only=True)
    board = BoardBreafSerializer(read_only=True)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
