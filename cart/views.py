from django.http import request
from products.models import Product
from django.shortcuts import get_object_or_404,redirect, render
from .cart import Cart
from .form import CartAddForm

def cart (request):
    cart = Cart(request)
    context = {'cart':cart, 'form':CartAddForm()}

    return render(request, 'cart/index.html', context)

def product_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        clean_form = form.cleaned_data
        cart.add(
            product=product, 
            quantity=clean_form['quantity'], 
            override=clean_form['override']
        )
    cart.save()
    return redirect('cart:detail')

