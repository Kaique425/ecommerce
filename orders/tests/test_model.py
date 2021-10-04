import pytest
from decimal import Decimal
from orders.models import Item, Orders

pytestmark = pytest.mark.django_db

def test_create(product, order):
    order = order()
    assert str(order) == f'Pedido {order.id}'
    assert order.__str__() == f'Pedido {order.id}'

    item = Item.objects.create(
            order = order,
            product = product,
            price = Decimal(10),
            quantity = 1
        )
    
    assert str(item) == str(item.id)