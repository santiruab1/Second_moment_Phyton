import pandas as pd

# Cargar los datasets usando rutas relativas
df_clientes = pd.read_csv('data/clientes.csv')
df_ventas = pd.read_csv('data/ventas.csv')

# Inspección rápida 
print("--- Clientes Info ---")
df_clientes.info() 
print("\n--- Ventas Info ---")
df_ventas.info()

def manejar_nulos(df, columnas, valor_reemplazo='Desconocido'):
    # Reemplaza valores nulos en las columnas indicadas
    for col in columnas:
        df[col] = df[col].fillna(valor_reemplazo)
    return df

# Inspección rápida antes de limpiar
print("Valores nulos antes de limpiar:")
print(df_clientes.isnull().sum())

# Aplicar la función
df_clientes = manejar_nulos(df_clientes, ['Nombre', 'Ciudad'])

# Inspección rápida después de limpiar
print("Valores nulos después de limpiar:")
print(df_clientes.isnull().sum())

