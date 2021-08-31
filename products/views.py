from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ProductsDetailView(DetailView):
    model = Product
    context_object_name = "product" 
    
    def get_slug_field(self):
        return self.slug_field
    

class ProductListView(ListView):
    model = Product
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(is_available=True)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searchbar = self.request.GET.get("searchbar") or ''
        if searchbar:
            context["product"] = context["product"].filter(name__istartswith=searchbar)
        context["searchbar"] = searchbar
        
        return context