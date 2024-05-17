from django.db import models

# Create your models here.
class SavingProduct(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
    fin_co_no = models.IntegerField() # 금융 회사 코드
    kor_co_nm = models.TextField()  # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융 상품 명
    etc_note = models.TextField()   # 기타 유의 사항
    join_deny = models.IntegerField()   # 가입 제한
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대조건
    mtrt_int = models.TextField() # 만기 후 이자율
    max_limit = models.IntegerField(null=True) # 최고 한도
    dcls_strt_day = models.CharField(max_length=10, null=True)
    dcls_end_day = models.CharField(max_length=10, null=True)
    fin_co_subm_day = models.TextField(null=True)

class SavingOption(models.Model):
    product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE) 
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형 명
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField()    # 최고 우대 금리
    save_trm = models.IntegerField() # 저축 기간
    rsrv_type = models.CharField(max_length=10) # 적립 유형
    rsrv_type_nm = models.TextField() # 적립 유형 명



class DepositProduct(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    fin_co_no = models.IntegerField() # 금융 회사 코드
    kor_co_nm = models.TextField()  # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융 상품 명
    etc_note = models.TextField()   # 기타 유의 사항
    join_deny = models.IntegerField()   # 가입 제한
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대조건
    mtrt_int = models.TextField() # 만기 후 이자율
    max_limit = models.IntegerField(null=True) # 최고 한도
    dcls_strt_day = models.CharField(max_length=10, null=True)
    dcls_end_day = models.CharField(max_length=10, null=True)
    fin_co_subm_day = models.TextField(null=True)

class DepositOption(models.Model):
    product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형 명
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField()    # 최고 우대 금리
    save_trm = models.IntegerField() # 저축 기간
