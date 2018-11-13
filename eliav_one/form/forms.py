from django import forms
from user_data import models

class Subscribe(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = "__all__"
