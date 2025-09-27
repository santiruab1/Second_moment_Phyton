import pandas as pd
# Cargar los datasets usando rutas relativas
df_clientes = pd.read_csv('data/clientes.csv')
df_ventas = pd.read_csv('data/ventas.csv')

# Inspección rápida 
print("--- Clientes Info ---")
df_clientes.info() 
print("\n--- Ventas Info ---")
df_ventas.info()