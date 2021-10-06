from orders.models import Orders
import factory
from faker import Faker
import faker.providers.address
Faker.seed(0)
faker = Faker(['pt_BR'])

class OrdersFactory (factory.django.DjangoModelFactory):
        cpf = faker.cpf()
        name = faker.name()
        email = faker.email()
        postal_code = faker.postcode()
        address = faker.street_name()
        number = faker.building_number()
        district = faker.bairro()
        state = faker.estado_sigla()
        city = faker.city()  

        class Meta:
            model = Orders