import os
import pandas as pd

def generate_deliver_orders_fact_data(config):
    routes_file_path = os.path.join(config['SILVER'], 'rutas.xlsx')
    ordenes_file_path = os.path.join(config['SILVER'], 'ordenes_de_entrega.xlsx')
    
    output_file_path = os.path.join(config['GOLD'], 'fact_ordenes_de_entrega.xlsx')

    df_rutas = pd.read_excel(routes_file_path)
    df_rutas = df_rutas[['RutaID', 'TiempoEstandar']]
    df = pd.read_excel(ordenes_file_path)

    df = df.merge(df_rutas, how='inner', on='RutaID')

    df['delta_entrega'] = df.apply(
        lambda x: x['TiempoReal'] - x['TiempoEstandar'],axis=1
    )

    df['sk_fecha'] = df['FechaEntrega'].dt.strftime('%Y%m%d')

    df.to_excel(output_file_path, index=False)

def silver_to_gold(config):
    generate_deliver_orders_fact_data(config)