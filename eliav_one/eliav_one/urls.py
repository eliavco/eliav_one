"""eliav_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sign_up.views import registration,user_login,hello,user_logout,special
urlpatterns = [
    path('', include("home.urls")),
    path('user_data/',include("user_data.urls")),
    path('admin/', admin.site.urls),
    path('form/',include("form.urls")),
    path('ord_form/',include("ordinary_form.urls")),
    path('sign_up/hello/',hello,name="hello"),
    path('sign_up/registration/',registration,name="regist"),
    path('sign_up/login/',user_login,name="login"),
    path('sign_up/logout/',user_logout,name="logout"),
    path('sign_up/special/',special,name="special"),
]
