from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from .serializers import DepositOptionSerializer, DepositProductSerializer, SavingOptionSerializer, SavingProductSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from .models import SavingProduct, SavingOption, DepositProduct, DepositOption
from django.contrib.auth import get_user_model
from django.db.models import Count, OuterRef, Subquery
from django.conf import settings
from accounts.models import SubscribedDeposit, SubscribedSaving
from django.db.models import Subquery

API_KEY = settings.PRODUCTS_API_KEY

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
        print(option)
        serializer = DepositOptionSerializer(data = option)
        product = DepositProduct.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    return Response( status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def deposit_products(request):
    if request.method == 'GET':
        product_infos = DepositOption.objects.all()
        product_info_serializer = DepositOptionSerializer(product_infos, many = True)
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
        print(baseinfo)
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
        product_infos = SavingOption.objects.all()
        product_info_serializer = SavingOptionSerializer(product_infos, many = True)
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


from django.db.models import Q, Count
from datetime import date

@api_view(['GET'])
def recommend_products(request):
    user = User.objects.get(id=request.user.id)

    # 나이 계산
    today = date.today()
    birthyear = int(user.birthday[:4]) if user.birthday else 0
    age = today.year - birthyear

    # 나이대, 연봉 범위, 목표 저축 범위를 계산하는 함수
    def get_range(value, ranges):
        for i, upper_bound in enumerate(ranges[1:], start=1):
            if value < upper_bound:
                return (ranges[i-1], upper_bound)
        return (ranges[-1], None)

    age_range = get_range(age, [0, 20, 40, 60])
    income_range = get_range(user.annual_income, [0,4000000000, 6000000000, 9000000000, 1500000000])
    saving_range = get_range(user.target_savings, [0,4000000000, 6000000000, 9000000000, 1500000000])
    age_start = today.year - age - 9
    age_end = today.year - age

    # 동일한 나이대, 연봉 범위, 목표 저축 범위에 속하는 User 필터링
    user_group = User.objects.filter(
        annual_income__range=income_range,
        target_savings__range=saving_range
    ).filter(
        birthday__isnull=False
    ).filter(
        Q(birthday__startswith=str(age_end)) |
        Q(birthday__startswith=str(age_start))
    )
    print(len(user_group))
    subscribed_savings = SubscribedSaving.objects.filter(
        user__in=user_group
    ).values('saving_option')

    subscribed_savings_count = subscribed_savings.annotate(
        subscribed_count=Count('saving_option')
    ).values('saving_option', 'subscribed_count')

    top_saving_products = SavingProduct.objects.annotate(
        subscribed_count=Subquery(
            subscribed_savings_count.filter(
                saving_option=OuterRef('savingoption__id')
            ).values('subscribed_count')[:1]
        )
    ).order_by('-subscribed_count')[:3]

    subscribed_deposits = SubscribedDeposit.objects.filter(
        user__in=user_group
    ).values('deposit_option')

    subscribed_deposits_count = subscribed_deposits.annotate(
        subscribed_count=Count('deposit_option')
    ).values('deposit_option', 'subscribed_count')

    top_deposit_products = DepositProduct.objects.annotate(
        subscribed_count=Subquery(
            subscribed_deposits_count.filter(
                deposit_option=OuterRef('depositoption__id')
            ).values('subscribed_count')[:1]
        )
    ).order_by('-subscribed_count')[:3]
    for product in top_saving_products:
        print(f"Saving Product: {product.fin_prdt_nm}, Subscribed Count: {product.subscribed_count}")

    for product in top_deposit_products:
        print(f"Deposit Product: {product.fin_prdt_nm}, Subscribed Count: {product.subscribed_count}")

    recommended_products_data = {
            'recommended_savings': SavingProductSerializer(top_saving_products, many=True).data,
            'recommended_deposits': DepositProductSerializer(top_deposit_products, many=True).data,
        }
    return Response({'recommended_products': recommended_products_data})
