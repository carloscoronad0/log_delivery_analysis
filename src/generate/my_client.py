from faker import Faker
from faker.providers import BaseProvider

import random

class MyClient(BaseProvider):
    types = ['Mayorista', 'Minorista']
    industries = ['Alimentos', 'Tecnologia', 'Farmaceutica', 'Vestimenta']

    def client_type(self) -> str:
        return random.choice(self.types)

    def client_industry(self) -> str:
        return random.choice(self.industries)
    
if __name__ == "__main__":
    fake = Faker()
    fake.add_provider(MyClient)
    for _ in range(5):
        print(fake.client_type())
        print(fake.client_industry())