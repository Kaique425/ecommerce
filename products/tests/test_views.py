from  pytest_django.asserts import assertTemplateUsed, assertQuerysetEqual
from products.tests.factories import ProductFactory
from django.urls import resolve, reverse
from ..models import Product
import pytest


pytestmark = pytest.mark.django_db

@pytest.fixture
def list_response(client):
     return client.get(reverse('product:list'))

     
class TestProductList():

    def test_status_code(self, list_response):
        assert list_response.status_code == 200

    def test_reverse_resolve(self):
        assert reverse('product:list') == '/'
        assert resolve('/').view_name == ('product:list')

    def test_template(self, list_response):
        assertTemplateUsed(list_response, 'products/product_list.html')

@pytest.fixture
def detail_response(client, product):
    return client.get(reverse('product:detail', kwargs={'slug':product.slug}))


class TestProductDetail():
    
    def test_status_code(self, client):
        product = ProductFactory(is_available=True)
        url = reverse('product:detail', kwargs={'slug': product.slug})
        response = client.get(url)
        assert response.status_code == 200

    def test_reverse_resolve(self, product):
        assert reverse('product:detail', kwargs={'slug':product.slug}) == f"/product/{product.slug}"
        assert resolve(f'/product/{product.slug}').view_name == "product:detail"

    def test_template(self, detail_response):
        assertTemplateUsed(detail_response, "products/product_detail.html")