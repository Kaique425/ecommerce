import pytest
from orders.tests.factories import OrdersFactory
from products.tests.factories import ProductFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def product():
    return ProductFactory()

@pytest.fixture
def order():
    return OrdersFactory()