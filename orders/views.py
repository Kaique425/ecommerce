from django.shortcuts import render, redirect
from django.urls import reverse
from orders.forms import OrdersForm
from django.views.generic import  CreateView
from cart.cart import Cart
from orders.models import Orders, Item



class OrderCreate(CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/ordercreate.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            self.request.session['order_id'] = order.id
            for item in cart:
                item = Item.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            return redirect(reverse('payment:create'))     
        return redirect(reverse('product:list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context