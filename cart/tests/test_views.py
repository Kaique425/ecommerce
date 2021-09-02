from django.contrib.sessions import middleware
from django.http.request import HttpRequest
from  django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed
import pytest

    
pytestmark = pytest.mark.django_db

@pytest.fixture
def cart_response(client):
    return  client.get(reverse('cart:detail'))

class TestCart():
    
    def test_home_url(self):
        assert reverse("cart:detail") == '/cart/'
        assert resolve('/cart/').view_name == 'cart:detail'

    def test_status_code(self, cart_response):
        assert cart_response.status_code == 200

    def test_template(self, cart_response):
        assertTemplateUsed(cart_response, "cart/index.html")

