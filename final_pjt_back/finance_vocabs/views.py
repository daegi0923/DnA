from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

BASE_URL = 'https://api.odcloud.kr/api/15044350/v1/uddi:88825fbb-6d63-4209-9e51-c777cb236f8b?page=1&perPage=10'
def index(request):
    url = BASE_URL
    response = requests.get(url).json()
    return JsonResponse(response)