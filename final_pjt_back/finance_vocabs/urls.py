from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-finance-voca/', views.save_finance_voca, name='save-finance-voca'),
    path('get_finance_vocas/', views.get_finance_vocas, name='get_finance_vocas')
]