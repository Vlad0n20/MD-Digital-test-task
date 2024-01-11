import factory.django
from faker import Faker

from .models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()

    class Meta:
        model = User
