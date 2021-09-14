from decimal import Decimal
import copy
from products.models import Product
from cart.form import CartAddForm

class Cart:

    def __init__(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}
        self.cart = request.session['cart']
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Product.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item['price'] = Decimal(item["price"])
            item['item_total_price'] = item['price'] * item['quantity']
            item['replace_quantity_form'] = CartAddForm(  initial={"quantity": item["quantity"], "override": True})
            yield item
            
    def save(self):
        self.session.modified = True

    def add (self, product, quantity=1,  override=False):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[str(product_id)] = {
                "price":str(product.price), 
                "quantity":0,
            }
        
        if override:
            self.cart[str(product_id)]["quantity"] += quantity
        else:
            self.cart[str(product_id)]["quantity"] += quantity
        
        self.save()

    def remove(self,product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    


    def get_total_price(self):
        return sum(Decimal(item["price"]) * item['quantity'] for item in self.cart.values())
