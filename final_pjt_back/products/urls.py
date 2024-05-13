from django.urls import include, path
from . import views


app_name = 'products'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name= 'save_deposit_products'),
    path('deposit-products/', views.deposit_products, name= 'deposit_products'),
    path('deposit-product-options/<int:deposit_product_id>/', views.deposit_product_options, name= 'deposit_product_options'),
    path('save-saving-products/', views.save_saving_products, name= 'save_saving_products'),
    path('saving-products/', views.saving_products, name= 'saving_products'),
    path('saving-product-options/<int:saving_product_id>/', views.saving_product_options, name= 'saving_product_options'),

]
