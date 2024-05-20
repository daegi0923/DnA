import requests
from .models import ExchangeRate
from django.http import JsonResponse
from .serializers import ExchangeRateSerializer
from datetime import datetime, timedelta

now = datetime.now()
BASE_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
def index(request):
    if now.hour < 11:
        search_data = now - timedelta(days=1)
    else:
        search_data = now

    if search_data.weekday() == 5:  # Saturday
        search_data -= timedelta(days=1)
    elif search_data.weekday() == 6:  # Sunday
        search_data -= timedelta(days=2)

    search_data_str = search_data.strftime('%Y%m%d')

    params = {
        'authkey': '1vdtuLiU3mNqNTMqu3VhqpXIEfb9HgCx',
        'searchdate': search_data_str,
        'data': 'AP01'
    }
    response = requests.get(BASE_URL, params=params).json()
    return JsonResponse(response, safe=False)



def save_exchanges(request):
    url = BASE_URL
    params = {
        'authkey': '1vdtuLiU3mNqNTMqu3VhqpXIEfb9HgCx',
        'data': 'AP01'
    }
    response = requests.get(url, params=params).json()

    for item in response:
        # Remove comma from number fields
        for field in ['ttb', 'tts', 'deal_bas_r', 'bkpr']:
            if ',' in item[field]:
                item[field] = float(item[field].replace(',', ''))
        # Serialize each item and save
        serialize = ExchangeRateSerializer(data=item)
        if serialize.is_valid(raise_exception=True):
            serialize.save()

    return JsonResponse({"message": "save okay!"})