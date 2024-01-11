import factory.django
from faker import Faker

from .models import Team
from apps.user.factories import UserFactory

fake = Faker()


class TeamFactory(factory.django.DjangoModelFactory):
    name = fake.name()

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)
        else:
            for _ in range(1, fake.random_int(min=1, max=4)):
                self.users.add(UserFactory.create())

    class Meta:
        model = Team
