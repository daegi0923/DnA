from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import SavingOption, DepositOption



class User(AbstractUser):
    GENDER_CHOICES = [
            ("남성", "남성"),
            ("여성", "여성"),
            ("미선택", "미선택"),
        ]

    BANK_CHOICES = [
            # ('모델에 설정할 값', '사람이 읽을수 있는 이름')
        ('우리은행','우리은행'),
        ('한국스탠다드차타드은행','한국스탠다드차타드은행'),
        ('대구은행','대구은행'),
        ('부산은행','부산은행'),
        ('광주은행','광주은행'),
        ('제주은행','제주은행'),
        ('전북은행','전북은행'),
        ('경남은행','경남은행'),
        ('중소기업은행','중소기업은행'),
        ('한국산업은행','한국산업은행'),
        ('국민은행','국민은행'),
        ('신한은행','신한은행'),
        ('농협은행','농협은행'),
        ('KEB하나은행','KEB하나은행'),
        ('수협은행','수협은행'),
        ('주식회사 카카오뱅크','주식회사 카카오뱅크'),
        ('주식회사 케이뱅크','주식회사 케이뱅크'),
        ('토스뱅크 주식회사','토스뱅크 주식회사'),
        ('기타','기타')
    ]
    PROVINCE_CHOICES= [
        ('서울특별시', '서울특별시'),
        ('인천광역시', '인천광역시'),
        ('대전광역시', '대전광역시'),
        ('대구광역시', '대구광역시'),
        ('광주광역시', '광주광역시'),
        ('부산광역시', '부산광역시'),
        ('울산광역시', '울산광역시'),
        ('세종특별자치시', '세종특별자치시'),
        ('경기도', '경기도'),
        ('강원도', '강원도'),
        ('충청북도', '충청북도'),
        ('충청남도', '충청남도'),
        ('경상북도', '경상북도'),
        ('경상남도', '경상남도'),
        ('전라북도', '전라북도'),
        ('전라남도', '전라남도'),
        ('제주특별자치도', '제주특별자치도'),
    ]
    target_savings = models.IntegerField(null=True) # 목표 저축금액
    annual_income = models.IntegerField(null=True) # 연 수입
    primary_bank = models.CharField(max_length=20, null=True, choices=BANK_CHOICES)  # 주 거래 은행
    subscribed_deposits = models.ManyToManyField(DepositOption, through='SubscribedDeposit')
    subscribed_savings = models.ManyToManyField(SavingOption, through='SubscribedSaving')
    birthday = models.CharField(max_length=8, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255, null=True, choices=PROVINCE_CHOICES)



class SubscribedSaving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saving_option = models.ForeignKey(SavingOption, on_delete=models.CASCADE, related_name='saving_subscribed')
    
class SubscribedDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit_option = models.ForeignKey(DepositOption, on_delete=models.CASCADE, related_name='deposit_subscribed')
