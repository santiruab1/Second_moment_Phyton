import pandas as pd

#Cargar los datasets usando rutas relativas
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
print("Valores nulos en clientes antes de limpiar:")
print(df_clientes.isnull().sum())

# Aplicar la función
df_clientes = manejar_nulos(df_clientes, ['Nombre', 'Ciudad'])

# Inspección rápida después de limpiar
print("Valores nulos en clientes después de limpiar:")
print(df_clientes.isnull().sum())

# Inspección rápida antes de limpiar ventas
print("Valores nulos en ventas antes de limpiar:")
print(df_ventas.isnull().sum())

# Aplicar la función a df_ventas
df_ventas = manejar_nulos(df_ventas, ['Producto', 'Cantidad'])

# Inspección rápida después de limpiar ventas
print("Valores nulos en ventas después de limpiar:")
print(df_ventas.isnull().sum())

# Función para estandarizar texto
def estandarizar_texto(df, columnas):
    """
    Convierte a minúsculas y elimina espacios extra en las columnas indicadas.
    """
    for col in columnas:
        df[col] = df[col].astype(str).str.lower().str.strip()
    return df

# Aplicar la función al DataFrame de ventas
df_ventas = estandarizar_texto(df_ventas, ['Producto'])

# Inspección rápida para validar estandarización
print("Primeros datos de ventas tras estandarizar texto:")
print(df_ventas.head(20))

# Aplicar la función al DataFrame de clientes
df_clientes = estandarizar_texto(df_clientes, ['Nombre', 'Ciudad'])

# Inspección rápida para validar estandarización en clientes
print("Primeros datos de clientes tras estandarizar texto:")
print(df_clientes.head(20))

def eliminar_simbolos(df, columnas, simbolos='$#€¥'):
    for col in columnas:
        for simbolo in simbolos:
            df[col] = df[col].astype(str).str.replace(simbolo, '', regex=False)
    return df

# Aplicar la función a los DataFrames
df_clientes = eliminar_simbolos(df_clientes, ['Nombre', 'Ciudad'])
df_ventas = eliminar_simbolos(df_ventas, ['Producto'])

# Filtrar ventas donde la cantidad sea mayor a 1
ventas_mayor_1 = df_ventas[df_ventas['Cantidad'].astype(int) > 1]
print("\nVentas con cantidad mayor a 1:")
print(ventas_mayor_1.head(20))

# Filtrar clientes de una ciudad específica, por ejemplo 'bogotá'
clientes_bogota = df_clientes[df_clientes['Ciudad'] == 'bogotá']
print("\nClientes de Bogotá:")
print(clientes_bogota.head(20))

# Filtrar ventas de un producto específico, por ejemplo 'televisor'
ventas_televisor = df_ventas[df_ventas['Producto'] == 'televisor']
print("\nVentas de Televisor:")
print(ventas_televisor.head(20))