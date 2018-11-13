from django.shortcuts import render
from form import forms
from home.views import index
# Create your views here.
def form_page(request):
    form = forms.Subscribe()
    if request.method == "POST":
        form = forms.Subscribe(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,"form/form_page.html",{"form":form})
