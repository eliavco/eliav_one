from django.urls import path
from user_data import views

urlpatterns = [
    path('',views.user_data,name="data"),
]
