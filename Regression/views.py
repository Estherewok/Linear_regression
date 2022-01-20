from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django import forms

class PredictPrice(forms.Form):
    Qty = forms.IntegerField()

class Predict_form(forms.Form):
    Quantity = forms.IntegerField(min_value=1)
    Price = forms.IntegerField(min_value=1)

def Index(request):
    form = Predict_form()

    #   Gets quantity to predict the price
    forms = PredictPrice()
    if request.method == 'POST':
        form = Predict_form(request.POST)
        if form.is_valid():
            Quantity = form.cleaned_data['Quantity']
            Price = form.cleaned_data['Price']
            
            # if no x_values in request.session
            if not request.session.get('x_values'):
                request.session['x_values'] = []
                request.session['y_values'] = []
            # get x and y values from session
            x_values = request.session['x_values']
            y_values = request.session['y_values']
            # add new data to x and y values 
            x_values.append(Quantity)
            y_values.append(Price)
            # update request.session x and y_values
            request.session['x_values'] = x_values
            request.session['y_values'] = y_values
            
    x_values = request.session.get('x_values') or []
    y_values = request.session.get('y_values') or []
    # merge x_values and y_values in a dictionary
    x_y_values = {x_values[idx]: y_values[idx] for idx in range(len(x_values))}
    return render(request, 'Regression/index.html', {'form' : form, 'xy' : x_y_values, 'predict' : forms})

def ClearData(request):
    # clears data that the user inserted
    request.session['x_values'] = []
    request.session['y_values'] = []
    # redirects/reverse users to the specified page(Index in this case)
    return HttpResponseRedirect(reverse('Index', args = []))

# Does the price prediction
import numpy as np
def LinearRegression(request):
    if request.method == 'POST':
        form = PredictPrice(request.POST)
        if form.is_valid():
            Qty = form.cleaned_data['Qty']
            x_values = request.session.get('x_values') or []
            y_values = request.session.get('y_values') or []

            # Predicts 
            Predicted = predict_price(x_values, y_values, Qty)
            return HttpResponse(Predicted)
def predict_price(x : list, y : list, new_product : float) -> float:
    """
    Using Linear regression to predict a new 'y' value giving previous learning data
    """
    n = len(x)
    x = np.array(x)
    y = np.array(y)
    slope = ((n * np.sum(x * y)) - (np.sum(x) * np.sum(y)))/ (n * np.sum(x ** 2) - (np.sum(x) ** 2))
    intercept = ((np.sum(y)) - (slope * np.sum(x)))/ n
    p_output = intercept + slope * new_product
    return p_output


