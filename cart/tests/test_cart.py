from decimal import Decimal
from products.tests.factories import ProductFactory
from ..cart import Cart
import pytest
from django.http import HttpRequest
from django.contrib.sessions.middleware import SessionMiddleware

def dummy_get_response():
    return None

@pytest.fixture
def http_request():
    request = HttpRequest()
    middleware = SessionMiddleware(dummy_get_response)
    middleware.process_request(request)
    return request

@pytest.fixture
def session(http_request):
    return http_request.session

@pytest.fixture
def cart(http_request):
    cart = Cart(http_request)
    return cart
    
pytestmark = pytest.mark.django_db


class TestCart():

    def test_create(self, http_request, session):
        Cart(http_request)

        assert session.modified
        assert session['cart'] == {}

    def test_add_product(self, http_request, session, product, cart):
        cart.add(http_request, product)

        assert session['cart'] == {
            str(product.id): {"price":str(product.price), "name": str(product.name)}
        }
        assert session.modified

    def test_get_total_price_method(self, cart, http_request, product):
        product_1 = ProductFactory()
        product_2 = ProductFactory()
        cart.add(http_request, product_1)
        cart.add(http_request, product_2)

        total_price = product_1.price + product_2.price
        assert cart.get_total_price() == total_price
        
