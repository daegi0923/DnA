from django.urls import include, path
from . import views


urlpatterns = [
    path('update-user/', views.update_info,),
]
