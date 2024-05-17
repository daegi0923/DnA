from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse
import pprint

# Create your views here.

BASE_URL = 'http://api.seibro.or.kr/openapi/service/FnTermSvc/getFinancialTermMeaning'
def index(request):
    params = {
        'serviceKey' : 'hpq%2ByfXRN6g5PmCCxN3ekB90v23I%2F14iaXedsUOzmhNcTbj0Bk%2FU8cFjSJSezmIw%2FzOg5oUPlm05%2B2g90B%2BaDg%3D%3D'
    }
    response = requests.get(BASE_URL, params=params)
    pp = pprint.PrettyPrinter(response.content)
    print(pp)