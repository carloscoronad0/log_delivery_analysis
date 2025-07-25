from generate.my_client import MyClient
from generate.my_product import MyProduct
from utils.config import DATA_GENERATOR

from faker import Faker
from datetime import date

import os
import random
import pandas as pd

Faker.seed(100)
random.seed(100)

fake = Faker()
fake.add_provider(MyClient)
fake.add_provider(MyProduct)

class DataGenerator:
    @staticmethod
    def generate_clientes(n=50) -> pd.DataFrame:
        data = []

        for i in range(1, n+1):
            data.append({
                "ClienteID": 1000 + i,
                "Nombre": fake.company(),
                "TipoCliente": fake.client_type(),
                "Industria": fake.client_industry(),
                "Direccion": fake.address()
            })

        return pd.DataFrame(data=data)

    @staticmethod
    def generate_productos(n=100) -> pd.DataFrame:
        data = []

        for i in range(1, n+1):
            industry = fake.client_industry()

            data.append({
                "ProductoID": 2000 + i,
                "Nombre": fake.product_name(industry),
                "Descripcion": fake.paragraph(),
                "PesoUnidad": fake.product_weight_dimension(industry),
                "DimensionUnidad": fake.product_weight_dimension(industry),
                "Industria": industry,
            })

        return pd.DataFrame(data=data)
    
    @staticmethod
    def generate_rutas(n=25) -> pd.DataFrame:
        data = []

        for i in range(1, n+1):
            data.append({
                "RutaID": 3000 + i,
                "Origen": fake.address(),
                "Destino": fake.address(),
                "Distancia": random.random() * 1000,
                "TiempoEstandar": random.randint(50, 180),
                "Region": random.choice(['Cochabamba', 'Santa Cruz', 'La Paz'])
            })

        return pd.DataFrame(data=data)
    
    @staticmethod
    def generate_conductores(n=30) -> pd.DataFrame:
        data = []

        for i in range(1, n+1):
            data.append({
                "ConductorID": 4000 + i,
                "Nombre": fake.name(),
                "Contacto": fake.phone_number(),
                "Edad": random.randint(25,50),
                "Region": random.choice(['Cochabamba', 'Santa Cruz', 'La Paz'])
            })

        return pd.DataFrame(data=data)

    @staticmethod
    def generate_ordenes_de_entrega(
        df_clientes: pd.DataFrame,
        df_rutas,
        df_conductores,
        config,
        n=10000
    ) -> pd.DataFrame:
        def get_status_by_date(deliver_date, state_dict) -> str:
            if deliver_date < date.today():
                return random.choice(state_dict['Pasado'])
            elif deliver_date == date.today():
                return random.choice(state_dict['Hoy'])
            else:
                return random.choice(state_dict['Futuro'])

        def get_drivers_by_route(df_rutas: pd.DataFrame, df_conductores: pd.DataFrame):
            df_aux_conductores = df_conductores.groupby('Region')['ConductorID'].apply(list).reset_index()
            df_aux_rutas = df_rutas.merge(df_aux_conductores, how='inner', on='Region')
            return df_aux_rutas[['RutaID', 'ConductorID']]

        id_clientes = df_clientes['ClienteID'].to_list()
        id_rutas_conductores = get_drivers_by_route(df_rutas, df_conductores)

        data = []

        for i in range(1, n+1):
            fecha_entrega = fake.date_between_dates(date_start="-3y", date_end="+5m")
            rutas_conductores_row = id_rutas_conductores.sample(n=1).iloc[0]

            data.append({
                "OrdenID": 5000 + i,
                "FechaEntrega": fecha_entrega,
                "ClienteID": random.choice(id_clientes),
                "RutaID": rutas_conductores_row['RutaID'],
                "ConductorID": random.choice(rutas_conductores_row['ConductorID']),
                "StatusOrden": get_status_by_date(fecha_entrega, config['STATUS_ORDENES']),
                "TiempoReal": random.randint(50, 180)
            })

        return pd.DataFrame(data=data)

    @staticmethod
    def save_to_excel(config: dict, df: pd.DataFrame, table: str):
        file_name = f"{table}.xlsx"
        file_path = os.path.join(config['OUTPUT'], file_name)

        df.to_excel(file_path, index=False)
