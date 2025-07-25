from faker import Faker
from faker.providers import BaseProvider

import random

class MyProduct(BaseProvider):
    product_names = {
        'Alimentos': ['Papas Fritas', 'Platano Frito', 'Cerveza', 'Gaseosa', 'Energizante', 'Pipocas'],
        'Tecnologia': ['Celular Samsung', 'Celular Honor', 'MacBook Pro', 'MacBook Air', 'Asus Zenbook', 'HP Legion'],
        'Farmaceutica': ['Omeprazol', 'Amoxicilina', 'Paracetamol', 'Vitaminas', 'Omega 3'],
        'Vestimenta': ['Backpack', 'Shirts', 'Pants', 'Jackets', 'Hoodies', 'Socks'],
    }

    product_multipliers = {
        'Alimentos': [10, 100, 1000],
        'Tecnologia': [10, 100, 1000],
        'Farmaceutica': [1, 10],
        'Vestimenta': [10, 100]
    }

    def product_name(self, industry: str) -> str:
        return random.choice(self.product_names[industry])
    
    def product_weight_dimension(self, industry: str) -> float:
        return random.random() * random.choice(self.product_multipliers[industry])

if __name__ == "__main__":
    fake = Faker()
    fake.add_provider(MyProduct)
    for _ in range(5):
        print(fake.client_type())
        print(fake.client_industry())