from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
# Create your views here.

class ProductsDetailView(DetailView):
    model = Product
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    context_object_name = "product"
    
    def get_queryset(self):
        return Product.objects.filter(is_available=True)