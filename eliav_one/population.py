import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eliav_one.settings')
import django
django.setup()
import random
from user_data.models import Users,Gender
from faker import Faker
fakegen = Faker()
genders = ['Man','Woman','Other']
def add_gender():
    g = Gender.objects.get_or_create(gender=random.choice(genders))[0]
    g.save()
    return g
# fake population script
def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_password = fakegen.password(length=10)
        fake_gender = add_gender()

        user = Users.objects.get_or_create(name=fake_name,email=fake_email,password=fake_password,gender=fake_gender)[0]

if __name__ == '__main__':
    d = int(input("How many users do you want to add?"))
    print("Populating Script!")
    populate(d)
    print("Populated!")
