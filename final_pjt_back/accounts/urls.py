from django.urls import include, path
from . import views


urlpatterns = [
    path('subscribe-saving/<int:saving_option_id>', views.subscribe_saving,),
    path('subscribe-deposit/<int:deposit_option_id>', views.subscribe_deposit,),
]
