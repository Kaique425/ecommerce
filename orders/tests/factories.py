from orders.models import Orders
import factory.fuzzy


class OrderFactory(factory.django.DjangoModelFactory):
    cpf = factory.fuzzy.FuzzyText(length=14)
    name = factory.fuzzy.FuzzyText()
    email = factory.fuzzy.FuzzyText()