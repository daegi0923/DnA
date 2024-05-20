from django.urls import include, path
from . import views


urlpatterns = [
    path('update-user/', views.update_info,),
    path('user-detail/<str:username>/', views.get_user_info,),
]
