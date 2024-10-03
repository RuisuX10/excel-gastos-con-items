import pandas as pd

# Cargar los DataFrames
df1 = pd.read_excel("comprobantes.xlsx", sheet_name="Sheet1", header=6)
df2 = pd.read_excel("gastos.xlsx", sheet_name="Sheet1", header=9)

# Agregar la columna 'detalle' en df2
df2['detalle'] = ''

# Obtener los últimos 6 valores de la columna 'Número' de df1
ultimos_numeros = df1['Número'].astype(str).str[-6:]

# Comparar y rellenar la columna 'detalle'
for index, row in df2.iterrows():
    neto_simp = row['Neto s/imp.']
    comprobante = str(row['Comprobante'])

    for numero in ultimos_numeros:
        # Buscar coincidencias en df1
        coincidencias = df1[df1['Número'].astype(str).str.endswith(numero)]
        if not coincidencias.empty:
            # Comparar Neto s/imp. con Unitario
            for _, match_row in coincidencias.iterrows():
                if neto_simp == match_row['Unitario']:
                    if numero in comprobante:
                        df2.at[index, 'detalle'] = match_row['Ítem']  # Asignar el valor de 'Ítem'
                        break  # Romper el bucle si se encuentra una coincidencia

# Guardar el DataFrame modificado en un nuevo archivo Excel
df2.to_excel("gastos_modificado.xlsx", index=False)

print("El archivo se ha guardado como 'gastos_modificado.xlsx'.")
