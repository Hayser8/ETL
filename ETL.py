import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
from pandas import json_normalize
from bson import ObjectId  # Para identificar ObjectId y convertirlos

# -------- PostgreSQL: Fuente relacional --------
print("Conectando a PostgreSQL...")
engine_pg = create_engine('postgresql+psycopg2://postgres:caca@localhost:5432/ETL')

print("Cargando datos de 'pais_envejecimiento'...")
df_sql = pd.read_sql('SELECT * FROM pais_envejecimiento', con=engine_pg)

# -------- MongoDB: Fuente no relacional --------
print("Conectando a MongoDB...")
mongo_uri = "mongodb+srv://garciasalasperezjulio:1234@lab1.ka8t9.mongodb.net/?retryWrites=true&w=majority&appName=Lab1"
client = MongoClient(mongo_uri)
db = client.get_database('ETL')  # Ajustá el nombre de la base si es necesario

colecciones = db.list_collection_names()
print("Colecciones encontradas:", colecciones)

df_mongo = pd.DataFrame()
for coleccion in colecciones:
    datos = list(db[coleccion].find({}))
    df_temp = json_normalize(datos)
    df_mongo = pd.concat([df_mongo, df_temp], ignore_index=True)

print("Datos cargados desde MongoDB:", df_mongo.shape)

# -------- Preprocesamiento / Unificación --------
print("Normalizando columnas para unir...")

# En df_sql la columna se llama 'pais'
df_sql['pais'] = df_sql['pais'].str.lower()

# En df_mongo la clave es 'país', así que la usamos para crear 'pais'
df_mongo['pais'] = df_mongo['país'].str.lower()
df_mongo.drop(columns=['país'], inplace=True)  # Opcional, para dejar solo 'pais'

# -------- Unión de ambas fuentes --------
print("Integrando datos en memoria...")
df_integrado = pd.merge(df_sql, df_mongo, on='pais', how='inner')

# -------- Convertir ObjectId a string --------
print("Convirtiendo ObjectId a string...")
df_integrado = df_integrado.applymap(lambda x: str(x) if isinstance(x, ObjectId) else x)

# -------- Carga al Data Warehouse --------
print("Cargando a PostgreSQL DWH...")
engine_dwh = create_engine('postgresql+psycopg2://postgres:caca@localhost:5432/ETL')
df_integrado.to_sql('datos_integrados_script', con=engine_dwh, if_exists='replace', index=False)

print("✅ Proceso completado exitosamente.")
