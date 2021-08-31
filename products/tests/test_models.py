from django.urls import reverse
import pytest 
from products.tests.factories import ProductFactory

pytestmark = pytest.mark.django_db

class TestProductModel():

    def test_str_name(self, product):
        assert str(product.name) == product.name

    def test_get_absolute_url(self, product):
        url = product.get_absolute_url()
        assert url == f'/product/{product.slug}'
        