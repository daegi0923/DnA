from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    cur_unit = models.CharField(max_length=10, null=True, blank=True)
    cur_nm = models.CharField(max_length=100, null=True, blank=True)
    ttb = models.FloatField(null=True, blank=True)
    tts = models.FloatField(null=True, blank=True)
    deal_bas_r =  models.FloatField(null=True, blank=True)
    bkpr =  models.FloatField(null=True, blank=True)
