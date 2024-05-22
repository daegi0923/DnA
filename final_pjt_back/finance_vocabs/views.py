from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse
import xml.etree.ElementTree as ET
from .serializers import VocasSerializer
from .models import Vocas
import re
from django.conf import settings

# Create your views here.

BASE_URL = 'http://api.seibro.or.kr/openapi/service/FnTermSvc/getFinancialTermMeaning'
API_KEY = settings.VOCA_API_KEY

def index(request):
    params = {
        'serviceKey': API_KEY,
        'numOfRows': 100,
        'pageNo': 3
    }

    response = requests.get(BASE_URL, params=params)
    print(response.content.decode('utf-8'))
    return HttpResponse(response.content, content_type='application/xml')

def save_finance_voca(request):
    params = {
        'serviceKey': API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    
    root = ET.fromstring(response.content)
    totalCount = int(root.find('.//totalCount').text)
    numOfRows = int(root.find('.//numOfRows').text)
    totalPages = (totalCount // numOfRows) + (1 if totalCount % numOfRows > 0 else 0)
    print(totalPages)

    for page in range(1, totalPages + 1):
        params['pageNo'] = int(page)
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            items = root.find('.//items')
        
            if items is not None:
                for item in items.findall('item'):
                    fnceDictNm = item.find('fnceDictNm').text
                    ksdFnceDictDescContent = ET.tostring(item.find('ksdFnceDictDescContent'), encoding='unicode', method='html')
                    # Check if the record already exists
                    if not Vocas.objects.filter(fnceDictNm=fnceDictNm).exists():
                        data = {
                            'fnceDictNm': fnceDictNm,
                            'ksdFnceDictDescContent': ksdFnceDictDescContent
                        }
                        serializer = VocasSerializer(data=data)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()

    return JsonResponse({"message": "save okay!"})


def get_finance_vocas(request):
    vocas = Vocas.objects.all()  # 모든 Voca 객체를 가져옵니다.
    serializer = VocasSerializer(vocas, many=True)  # 여러 개의 객체를 직렬화하기 위해 many=True를 설정합니다.
    return JsonResponse(serializer.data, safe=False)  # 직렬화된 데이터를 JSON 응답으로 반환합니다.