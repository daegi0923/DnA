from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .serializer import SavingProductOptionsSerializer, SavingProductsSerializer, TopRateOptionsSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from .models import SavingProducts, SavingProductOptions
from django.db.models import Max


API_KEY = '8b4f8a3763090ac99ffff049e70b2e2c'
API_URL = f'https://finlife.fss.or.kr/finlifeapi/SavingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

# Create your views here.



@api_view(["GET"])
def save_saving_products(request):
    data = requests.get(API_URL).json().get('result')
    baseinfos = data.get('baseList')
    options = data.get('optionList')
    # print(options)
    for baseinfo in baseinfos:
        serializer = SavingProductsSerializer(data = baseinfo)
        if serializer.is_valid():
            serializer.save()
    for option in options:
        # print(option)
        serializer = SavingProductOptionsSerializer(data = option)
        product = SavingProducts.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    return Response( status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def saving_products(request):
    if request.method == 'GET':
        product_infos = SavingProducts.objects.all()
        product_info_serializer = SavingProductsSerializer(product_infos, many = True)
        print(product_info_serializer)
        return Response(product_info_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        product = SavingProductsSerializer(data = request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_200_OK)
        else:
            return Response({"messege" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def saving_product_options(request, fin_prdt_cd):
    options = SavingProductOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
    serializer = SavingProductOptionsSerializer(options, many = True)
    print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)
