from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from .serializers import UserUpdateSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
@api_view(['PUT'])
def update_info(request):
    user = get_user_model().objects.get(id=request.user.id)
    if request.method == 'PUT':
        serializer = UserUpdateSerializer(data=request.data, partial=True, instance=request.user)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('저장됨saved!')
            return Response(serializer.data, status=status.HTTP_201_CREATED)