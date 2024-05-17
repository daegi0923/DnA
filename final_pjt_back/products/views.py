from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from .serializer import DepositOptionSerializer, DepositProductSerializer, SavingOptionSerializer, SavingProductSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from .models import SavingProduct, SavingOption, DepositProduct, DepositOption


API_KEY = '8b4f8a3763090ac99ffff049e70b2e2c'

# Create your views here.



@api_view(["GET"])
def save_deposit_products(request):
    API_URL = f'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    data = requests.get(API_URL).json().get('result')
    baseinfos = data.get('baseList')
    options = data.get('optionList')
    # print(options)
    for baseinfo in baseinfos:
        serializer = DepositProductSerializer(data = baseinfo)
        if serializer.is_valid():
            serializer.save()
    for option in options:
        # print(option)
        serializer = DepositOptionSerializer(data = option)
        product = DepositProduct.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    return Response( status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def deposit_products(request):
    if request.method == 'GET':
        product_infos = DepositProduct.objects.all()
        product_info_serializer = DepositProductSerializer(product_infos, many = True)
        print(product_info_serializer)
        return Response(product_info_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        # print('data', request.data)
        product = DepositProductSerializer(data = request.data)
        # print(product)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_200_OK)
        else:
            return Response({"messege" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def deposit_product_options(request, deposit_product_id):
    deposit_product = DepositProduct.objects.get(id = deposit_product_id)
    serializer = DepositProductSerializer(deposit_product)
    print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def save_saving_products(request):
    API_URL = f'https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    data = requests.get(API_URL).json().get('result')
    baseinfos = data.get('baseList')
    options = data.get('optionList')
    # print(options)
    for baseinfo in baseinfos:
        serializer = SavingProductSerializer(data = baseinfo)
        if serializer.is_valid():
            serializer.save()
    for option in options:
        # print(option)
        serializer = SavingOptionSerializer(data = option)
        product = SavingProduct.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    return Response( status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def saving_products(request):
    if request.method == 'GET':
        product_infos = SavingProduct.objects.all()
        product_info_serializer = SavingProductSerializer(product_infos, many = True)
        print(product_info_serializer)
        return Response(product_info_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        # print('data', request.data)
        product = SavingProductSerializer(data = request.data)
        # print(product)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_200_OK)
        else:
            return Response({"messege" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def saving_product_options(request, saving_product_id):
    saving_product = SavingProduct.objects.get(id = saving_product_id)
    options = SavingOption.objects.filter(fin_prdt_cd = saving_product.fin_prdt_cd)
    serializer = SavingOptionSerializer(options, many = True)
    print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)

