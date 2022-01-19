from django.shortcuts import render
# Create your views here.
from django import forms

class Predict_form(forms.Form):
    Quantity = forms.IntegerField(min_value=1)
    Price = forms.DecimalField(min_value=1)

def Index(request):
    form = Predict_form()
    return render(request, 'Regression/index.html', {'form' : form})

