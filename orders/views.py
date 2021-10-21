from django.shortcuts import render, redirect
from django.urls import reverse
from orders.forms import OrdersForm
from django.views.generic import  CreateView
from cart.cart import Cart
from orders.models import Item



class OrderCreate(CreateView):
    form_class = OrdersForm
    template_name = 'orders/ordercreate.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            for item in cart:
                item = Item.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                cart.clear()
            return render(self.request, 'payments/create.html')     
        return redirect(reverse('product:list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context