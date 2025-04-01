import pandas as pd

# Cargar los datasets originales
poblacion_df = pd.read_csv("pais_poblacion.csv")
envejecimiento_df = pd.read_csv("pais_envejecimiento.csv")

# 1. Limpiar envejecimiento_df: quedarnos solo con lo útil
envejecimiento_clean = envejecimiento_df[["nombre_pais", "tasa_de_envejecimiento"]].copy()
envejecimiento_clean = envejecimiento_clean.rename(columns={"nombre_pais": "pais"})

# 2. Hacer merge con pais_poblacion.csv (ambos tienen columna 'pais')
df_final = pd.merge(poblacion_df, envejecimiento_clean, on="pais", how="inner")

# 3. Guardar archivo limpio
df_final.to_csv("dataset_limpio.csv", index=False)

print("✅ Dataset limpio guardado como 'dataset_limpio.csv'")
