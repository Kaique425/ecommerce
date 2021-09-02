import factory 
import factory.fuzzy
from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)
    product_image = factory.django.ImageField()
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    is_available = factory.Faker("pybool")

    class Meta:
        model = Product