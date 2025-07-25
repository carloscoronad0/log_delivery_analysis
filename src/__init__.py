from generate.synthetic_data_generator import DataGenerator as dg
from pipeline.bronze_to_silver import bronze_to_silver
from pipeline.silver_to_gold import silver_to_gold
from utils.config import DATA_GENERATOR

# df_clientes = dg.generate_clientes()
# dg.save_to_excel(DATA_GENERATOR, df_clientes, 'clientes')

# df_productos = dg.generate_productos()
# dg.save_to_excel(DATA_GENERATOR, df_productos, 'productos')

# df_rutas = dg.generate_rutas()
# dg.save_to_excel(DATA_GENERATOR, df_rutas, 'rutas')

# df_conductores = dg.generate_conductores()
# dg.save_to_excel(DATA_GENERATOR, df_conductores, 'conductores')

# df_ordenes = dg.generate_ordenes_de_entrega(
#                 df_clientes,
#                 df_rutas,
#                 df_conductores,
#                 DATA_GENERATOR
#             )
# dg.save_to_excel(DATA_GENERATOR, df_ordenes, 'ordenes_de_entrega')

# DATA PIPELINE
bronze_to_silver(DATA_GENERATOR)
silver_to_gold(DATA_GENERATOR)