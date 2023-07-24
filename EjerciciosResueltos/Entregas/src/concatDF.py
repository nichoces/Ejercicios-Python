# Importamos las librerias
import pandas as pd


# LEEMOS EL DATAFRAME

# df = pd.read_csv('data/temperaturas.csv')

# ELIMINAMOS LAS COLUMNAS QUE NO NOS INTERESAN

# df=df.drop(['indicativo','provincia','sol'],axis=1)

# CONVERTIMOS LOS CAMPOS EN LO QUE NOS INTERESA

# df['tmax'] = df['tmax'].str.replace(',', '.').astype(float)
# df['tmin'] = df['tmin'].str.replace(',', '.').astype(float)
# df['tmed'] = df['tmed'].str.replace(',', '.').astype(float)


# SOBREECRIBIMOS EL UNA VEZ ACTUALIZADAS LAS COLUMNAS

# df.to_csv('data/temperaturas.csv', index=False)