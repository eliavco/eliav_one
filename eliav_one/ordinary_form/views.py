from django.shortcuts import render
from home.views import index
from ordinary_form import forms
# Create your views here.
def form_page(request):
    form = forms.Survey()
    if request.method == "POST":
        form = forms.Survey(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            opinion = form.cleaned_data['opinion']
            print(f"Name: {name}")
            print(f"Opinion: {opinion}")
    return render(request,"ordinary_form/ord_form.html",context={"form":form})
