from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    target_savings = models.IntegerField(null=True) # 목표 저축금액
    annual_income = models.IntegerField(null=True) # 연 수입
    primary_bank = models.CharField(max_length=20, null=True)  # 주 거래 은행