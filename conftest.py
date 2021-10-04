import pytest
from products.tests.factories import ProductFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def product():
    return ProductFactory()

