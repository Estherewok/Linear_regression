from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name = 'Index'),
    path('clear/', views.ClearData, name = 'ClearData'),
    path('Predict/', views.LinearRegression, name = 'LinearRegression')
]