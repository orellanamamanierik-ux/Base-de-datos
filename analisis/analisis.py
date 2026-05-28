# Importa pandas
import pandas as pd

# Lee el archivo CSV
df = pd.read_csv("Indian_Student_AI_Dataset.csv")

# Mensaje de carga
print("okey! Archivo cargado correctamente")

# Muestra primeras filas
print(df.head())

# Obtiene filas y columnas
filas, columnas = df.shape

# Muestra tamaño del dataframe
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

# Titulo del analisis
print("---Analisis Avansado de Datos---")

# Filtra lenguajes que empiezan con C+
filtro_avanzado = df['preferred_programming_language'].str.startswith('C+', na=False)

# Guarda datos filtrados
df_filtrado = df[filtro_avanzado]

# Cuenta registros filtrados
total_registros = df_filtrado['preferred_programming_language'].count()

# Muestra cantidad
print(f"Cantidad de envios de tecnologia 'advance' {total_registros}")

# Suma valores de bienestar mental
suma_dinero = df_filtrado['mental_wellbeing_score'].sum()

# Muestra suma total
print(f"valor total de este comercio: USD {suma_dinero:.2f} millions")


# Verifica si el valor es muy alto
if suma_dinero > 500:
    print("Alerta: El volumen de mercado es critico")
    print("Requiere revision inmediata")

# Verifica si el valor es moderado
elif suma_dinero > 200:
    print("Aviso: volumen mercado moderado/alto")
    print("Monitorear comportamiento proximo trimestre")

# Caso contrario
else:
    print("Estado: volumen de mercado bajo")
    print("No se requiere accion profesional")