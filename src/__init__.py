from generate.synthetic_data_generator import DataGenerator as dg
from utils.config import DATA_GENERATOR

df_clientes = dg.generate_clientes()
dg.save_to_excel(DATA_GENERATOR, df_clientes, 'clientes')

df_productos = dg.generate_productos()
dg.save_to_excel(DATA_GENERATOR, df_productos, 'productos')

df_rutas = dg.generate_rutas()
dg.save_to_excel(DATA_GENERATOR, df_rutas, 'rutas')

df_conductores = dg.generate_conductores()
dg.save_to_excel(DATA_GENERATOR, df_conductores, 'conductores')