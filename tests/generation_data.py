import random
from faker import Faker


class GenerationData:
    def generation_email(self):
        faker = Faker()
        email = faker.email()
        return email

    def generation_password(self):
        password = random.randint(100000, 999999)
        return password
