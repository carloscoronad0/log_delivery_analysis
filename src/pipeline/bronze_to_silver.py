import pandas as pd
import os

def validate_client_table(config, table_name):
    file_name = f"{table_name}.xlsx"
    input_file_path = os.path.join(config['OUTPUT'], file_name)
    ouput_file_path = os.path.join(config['SILVER'], file_name)

    df = pd.read_excel(input_file_path)

    # General validations
    df.drop_duplicates(subset=['ClienteID'], inplace=True)
    df.dropna(subset=['ClienteID'], inplace=True)

    # Specific validations
    df['valid_industry'] = df.apply(
        lambda x: not (x['TipoCliente'] == 'Minorita' and x['Industria'] == 'Farmaceutica'), axis=1
    )
    df['TipoCliente'] = df.apply(lambda x: x['TipoCliente'] if x['valid_industry'] else 'Mayorista', axis=1)

    df.to_excel(ouput_file_path, index=False)

def validate_driver_table(config, table_name, route_name):
    file_name = f"{table_name}.xlsx"
    validation_file_name = f"{route_name}.xlsx"

    input_file_path = os.path.join(config['OUTPUT'], file_name)
    output_file_path = os.path.join(config['SILVER'], file_name)
    validation_file_path = os.path.join(config['OUTPUT'],validation_file_name)

    df = pd.read_excel(input_file_path)
    df_rutas = pd.read_excel(validation_file_path)

    # General validations
    df.drop_duplicates(subset=['ConductorID'], inplace=True)
    df.dropna(subset=['ConductorID'], inplace=True)

    # Specific validations
    count_regions = df.groupby('Region').agg('count').reset_index()
    print(f"Numero de regiones para conductores: {count_regions.shape[0]}")

    route_regions = df_rutas.merge(count_regions, how='left', on='Region')
    route_regions = route_regions[['Region', 'ConductorID']].groupby('Region').sum().reset_index()
    print(route_regions)

    df.to_excel(output_file_path, index=False)

def validate_route_table(config, table_name):
    file_name = f"{table_name}.xlsx"
    input_file_path = os.path.join(config['OUTPUT'], file_name)
    output_file_path = os.path.join(config['SILVER'], file_name)

    df = pd.read_excel(input_file_path)

    # General validations
    df.drop_duplicates(subset=['RutaID'], inplace=True)
    df.dropna(subset=['RutaID'], inplace=True)

    df.to_excel(output_file_path, index=False)
 
def validate_deliver_orders_table(config, table_name):
    file_name = f"{table_name}.xlsx"
    input_file_path = os.path.join(config['OUTPUT'], file_name)
    output_file_path = os.path.join(config['SILVER'], file_name)

    df = pd.read_excel(input_file_path)

    # General validations
    df.drop_duplicates(subset=['OrdenID'], inplace=True)
    df.dropna(subset=['OrdenID'], inplace=True)

    df.to_excel(output_file_path, index=False)

def bronze_to_silver(config):
    validate_client_table(config, 'clientes')
    validate_driver_table(config, 'conductores', 'rutas')
    validate_route_table(config, 'rutas')
    validate_deliver_orders_table(config, 'ordenes_de_entrega')