from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import SavingOption, DepositOption
class User(AbstractUser):
    target_savings = models.IntegerField(null=True) # 목표 저축금액
    annual_income = models.IntegerField(null=True) # 연 수입
    primary_bank = models.CharField(max_length=20, null=True)  # 주 거래 은행
    subscribed_deposits = models.ManyToManyField(DepositOption, through='SubscribedDeposit')
    subscribed_savings = models.ManyToManyField(SavingOption, through='SubscribedSaving')

class SubscribedSaving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saving_option = models.ForeignKey(SavingOption, on_delete=models.CASCADE)
    
class SubscribedDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit_option = models.ForeignKey(DepositOption, on_delete=models.CASCADE)
