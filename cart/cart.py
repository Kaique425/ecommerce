from decimal import Decimal
import copy
from products.models import Product

class Cart:

    def __init__(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}
        self.cart = request.session['cart']

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Product.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            yield item

    def save(self, request):
        request.session.modified = True

    def add (self, request, product):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[str(product_id)] = {"price":str(product.price), "name":str(product.name)}
            self.save(request)
    

    def get_total_price(self):
        return sum(Decimal(item["price"]) for item in self.cart.values())

    