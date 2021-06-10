from django.urls import path
from .views import RegisterStudent, home, UpdateRegisterStudent, products
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('RegisterStudent/', RegisterStudent, name='RegisterStudent'),
    path('Update/', UpdateRegisterStudent, name='Update'),
    path('products/', products, name='products'),
    path('jsoncall/',views.jsoncall,name='jsoncall'),
]
