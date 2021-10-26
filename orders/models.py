from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields.related import ForeignKey
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
from products.models import Product


class Orders(models.Model):

    cpf = BRCPFField("CPF")
    name = models.CharField("Nome Completo", max_length=256)
    email = models.EmailField("Email")
    postal_code = BRPostalCodeField("CEP")
    address = models.CharField("Endereço", max_length=250)
    number = models.CharField("Numero", max_length=250)
    compliment = models.CharField("Complemento", max_length=250, blank=True)
    district = models.CharField("Bairro", max_length=250)
    state = BRStateField("Estado")
    city = models.CharField("Cidade", max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'Pedido {self.id}'

    
    def get_total_price(self):
        return sum(item.get_item_price() for item in self.item.all() )

    def get_description(self):
        return ", ".join([f'{Item.quantity}x {Item.product.name}' for item in self.items.all()])


class Item(models.Model):
    order = ForeignKey(Orders, related_name="Item", on_delete=models.CASCADE)
    product = ForeignKey(Product, related_name="order_item", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(
    validators= [
            MinValueValidator(1),
            MaxValueValidator(20)
    ])

    def __str__(self):
        return str(self.id)

    
    def get_item_price(self):
        return self.price * self.quantity