from django.db import models

# Create your models here.
class Vocas(models.Model):
    fnceDictNm = models.CharField(max_length=200)
    ksdFnceDictDescContent = models.CharField(max_length=4000)