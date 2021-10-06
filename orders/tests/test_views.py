import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


pytestmark = pytest.mark.django_db


def test_reverse_resolve():
    assert reverse('orders:create') == '/orders/create/'
    assert resolve('/orders/create/').view_name == 'orders:create'

def test_status_code(client):
    response  = client.get(reverse('orders:create'))
    assert response.status_code == 200

def test_order_create(client,product, order):
    form = {
        'cpf' : order.cpf,
        'name' : order.name,
        'email' : order.email,
        'postal_code' : order.postal_code,
        'address' : order.address,
        'number' : order.number,
        'district' : order.district,
        'state' : order.state,
        'city' : order.city 
    }
    response = client.post(reverse("orders:create"), data=form , follow=True)
    assertTemplateUsed(response, "products/product_list.html")

    client.post(
        reverse("cart:add", kwargs={"id": product.id}),
        data={"quantity": 1, "override": False},
    )

    response = client.post(reverse("orders:create"), form , follow=True)
    assertTemplateUsed(response, "orders/order_created.html")