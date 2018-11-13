from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {
        'insert':"Hi! I'm from views.py",
        'text':"hello world!",
        'number':100
    }
    return render(request,"home/index.html",context=my_dict)
