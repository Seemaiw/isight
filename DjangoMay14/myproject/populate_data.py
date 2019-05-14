import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django

django.setup()

from first_app.models import TestUser,Profile
from faker import Faker

fakegen = Faker()


def populate(N):
    for i in range(N):
        first_name = fakegen.name()
        last_name = fakegen.name()
        email = fakegen.email()
        address = fakegen.address()
        phone_number = fakegen.phone_number()

        t = TestUser.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        Profile.objects.get_or_create(testuser=t, address=address, phone_number=phone_number)[0]


if __name__ == '__main__':
    print('Populating')
    populate(5)
    print('Complete')

