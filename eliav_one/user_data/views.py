from django.shortcuts import render
from user_data.models import Gender,Users
# Create your views here.
def user_data(request):
    table = Users.objects.order_by("name")
    my_dict = {'users_table':table}
    return render(request,"user_data/data.html",context=my_dict)
