from django.urls import path
from ordinary_form import views
urlpatterns = [
    path('',views.form_page,name="ord_form"),
]
