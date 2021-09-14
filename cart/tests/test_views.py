from django.contrib.sessions import middleware
from django.http.request import HttpRequest
from  django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed
import pytest

    
pytestmark = pytest.mark.django_db

@pytest.fixture
def cart_detail_response(client):
    return  client.get(reverse('cart:detail'))

@pytest.fixture
def cart_add_response(client, product):
    return client.get(reverse('cart:add', kwargs={'id':product.id}))


class TestHomeSView():
    
    def test_home_url(self):
        assert reverse("cart:detail") == '/cart/'
        assert resolve('/cart/').view_name == 'cart:detail'

    def test_status_code(self, cart_detail_response):
        assert cart_detail_response.status_code == 200

    def test_template(self, cart_detail_response):
        assertTemplateUsed(cart_detail_response, "cart/index.html")


class TestAddView():

    def test_add_ulr(self,product):
        assert reverse('cart:add', kwargs= {'id': product.id}) == f'/cart/add/{product.id}'
        assert resolve(f'/cart/add/{product.id}').view_name == 'cart:add'

    def test_add_status_code(self, cart_add_response):
        assert cart_add_response.status_code == 302
        assert cart_add_response.url == '/cart/'

class TestRemoveView():
    
    def test_remove_url(self, product):
        assert reverse('cart:remove', kwargs= {'id': product.id}) == f'/cart/remove/{product.id}'
        assert resolve(f'/cart/remove/{product.id}').view_name == 'cart:remove'

    def test_remove_status_code(self, client, product):
        client.post(
            reverse("cart:add", kwargs={"id": product.id}),
            data={"quantity": 1, "override": False},
        )

        response = client.post(
            reverse('cart:remove', kwargs= {'id': product.id})
            )
        assert response.status_code == 302
        assert response.url == '/cart/'