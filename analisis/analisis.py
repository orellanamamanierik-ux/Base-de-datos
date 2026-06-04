# Importar librerías
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("Indian_Student_AI_Dataset.csv")

# --------------------------------------------
# CARGA Y EXPLORACIÓN DE DATOS
# --------------------------------------------

print("¡Archivo cargado correctamente!\n")

# Mostrar primeras filas
print(df.head())

# Obtener filas y columnas
filas, columnas = df.shape

# Mostrar tamaño del DataFrame
print(f"\nEl DataFrame tiene {filas} filas y {columnas} columnas")

# Título del análisis
print("\n--- ANÁLISIS AVANZADO DE DATOS ---")

# --------------------------------------------
# FILTRO DE DATOS
# --------------------------------------------

# Filtrar lenguajes que comienzan con C+
filtro = df["preferred_programming_language"].str.startswith("C+", na=False)

# Guardar datos filtrados
df_filtrado = df[filtro]

# Contar registros filtrados
total_registros = df_filtrado["preferred_programming_language"].count()

# Mostrar cantidad
print(f"Cantidad de estudiantes que utilizan C+: {total_registros}")

# Sumar valores de bienestar mental
suma_bienestar = df_filtrado["mental_wellbeing_score"].sum()

# Mostrar suma
print(f"Suma total de bienestar mental: {suma_bienestar:.2f}")

# --------------------------------------------
# ANÁLISIS CONDICIONAL
# --------------------------------------------

if suma_bienestar > 500:
    print("\nAlerta: nivel de bienestar acumulado muy alto")
    print("Se recomienda revisar los resultados.")
elif suma_bienestar > 200:
    print("\nAviso: nivel de bienestar acumulado moderado")
    print("Continuar monitoreando los datos.")
else:
    print("\nEstado: nivel de bienestar acumulado bajo")
    print("No se requiere acción inmediata.")

# --------------------------------------------
# GRÁFICO DE BARRAS
# --------------------------------------------

print("\nGenerando gráfico de barras...")

sns.set_theme(style="whitegrid")

datos_barras = (
    df.groupby("preferred_programming_language")["mental_wellbeing_score"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=datos_barras.index,
    y=datos_barras.values,
    palette="Blues_d"
)

plt.title(
    "Bienestar mental por lenguaje de programación",
    fontsize=14
)

plt.xlabel(
    "Lenguaje de programación",
    fontsize=11
)

plt.ylabel(
    "Total de mental_wellbeing_score",
    fontsize=11
)

plt.xticks(rotation=40)

plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=300)
plt.close()

print("Gráfico de barras guardado exitosamente.")

# --------------------------------------------
# GRÁFICO DE TORTA
# --------------------------------------------

print("\nGenerando gráfico de torta...")

datos_torta = (
    df.groupby("preferred_programming_language")["mental_wellbeing_score"]
      .sum()
      .nlargest(5)
)

plt.figure(figsize=(7, 7))

plt.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2")[0:5],
    startangle=140,
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 2
    }
)

plt.title("Distribución del bienestar mental por lenguaje")

plt.savefig("grafico_torta.png", dpi=300)
plt.close()

print("Gráfico de torta guardado exitosamente.")

# --------------------------------------------
# FIN DEL PROGRAMA
# --------------------------------------------

print("\nAnálisis finalizado correctamente.")