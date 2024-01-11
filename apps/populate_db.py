import random
from faker import Faker

from apps.group.models import Team
from apps.user.models import User

fake = Faker()


def create_users(count=10):
    for i in range(count):
        new_user = User.objects.create_user(
            username=fake.name(),
            email=fake.email(),
        )
        new_user.set_password('1')
        new_user.save()


def create_teams(count=10):
    users_ids = User.objects.values_list('id', flat=True)
    for i in range(count):
        new_team = Team.objects.create(
            name=fake.name(),
            description=fake.text(),
        )
        new_team.users.set(random.sample(list(users_ids), random.randint(2, len(users_ids) - 1)))


def run():
    create_users()
    create_teams()
