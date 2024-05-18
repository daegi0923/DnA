from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from .serializer import DepositOptionSerializer, DepositProductSerializer, SavingOptionSerializer, SavingProductSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from .models import SavingProduct, SavingOption, DepositProduct, DepositOption
from django.contrib.auth import get_user_model


API_KEY = '8b4f8a3763090ac99ffff049e70b2e2c'

# Create your views here.
User = get_user_model()



@api_view(["GET"])
def save_deposit_products(request):
    API_URL = f'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    data = requests.get(API_URL).json().get('result')
    baseinfos = data.get('baseList')
    options = data.get('optionList')
    # print(options)
    for baseinfo in baseinfos:
        serializer = DepositProductSerializer(data = baseinfo)
        # print(baseinfo)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('save success')
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
        # print(product_info_serializer)
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
    # print(serializer)
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
    return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def saving_products(request):
    if request.method == 'GET':
        product_infos = SavingProduct.objects.all()
        product_info_serializer = SavingProductSerializer(product_infos, many = True)
        # print(product_info_serializer)
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
    serializer = SavingProductSerializer(saving_product)
    # print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET","POST"])
def subscribe_saving(request, saving_option_id):
    saving_option = SavingOption.objects.get(id=saving_option_id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        if saving_option in user.subscribed_savings.all():
            user.subscribed_savings.remove(saving_option)
            return Response({"message" : "subscribed canceled"},status=status.HTTP_200_OK)
        else:
            user.subscribed_savings.add(saving_option)
            return Response({"message" : "subscribed!"}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        is_subscribed = {}
        is_subscribed['is_subscribed'] = saving_option in user.subscribed_savings.all()
        return Response(is_subscribed, status=status.HTTP_200_OK)

        
@api_view(["GET","POST"])
def subscribe_deposit(request, deposit_option_id):
    deposit_option = DepositOption.objects.get(id=deposit_option_id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        if deposit_option in user.subscribed_deposits.all():
            user.subscribed_deposits.remove(deposit_option)
            return Response({"message" : "subscribed canceled"}, status=status.HTTP_200_OK)

        else:
            user.subscribed_deposits.add(deposit_option)
            return Response({"message" : "subscribed"}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        is_subscribed = {}
        is_subscribed['is_subscribed'] = deposit_option in user.subscribed_deposits.all()
        return Response(is_subscribed, status=status.HTTP_200_OK)

