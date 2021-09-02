from products.models import Product
from django.shortcuts import get_object_or_404,redirect, render
from .cart import Cart
from .form import CartAddForm
from cart import form

def cart (request):
    cart = Cart(request)
    context = {'cart':cart, 'form':CartAddForm()}
    return render(request, 'cart/index.html', context)

def product_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(request,product)
    cart.save(request)
    return redirect('cart:detail')

