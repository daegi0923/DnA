from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-exchanges/', views.save_exchanges, name='save_exchanges'),
]