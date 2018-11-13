from django.urls import path
from form import views
urlpatterns = [
    path('',views.form_page,name="form_page"),
]
