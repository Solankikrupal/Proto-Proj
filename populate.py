import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')


import django
django.setup()

from AppTwo.models import User
from faker import Faker

fake  = Faker()

def populate(n = 5):
    for entry in range(n):

        names = fake.name().split(' ')
        email = fake.email()

        User_go = User.objects.get_or_create(first_name = names[0],last_name = names[1],e_mail = email)

if __name__ == '__main__':
    print('Populating')
    populate(10)
    print('completed')
