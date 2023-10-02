import pandas as pd
from geopy.geocoders import Nominatim

# Crea una instancia del geocodificador de Nominatim
geolocator = Nominatim(user_agent="GoogleMaps")

# Lee el archivo Excel
df = pd.read_excel("/Users/maria/Documents/ITBA MARIA/3 1Q/Visualizacion de la informacion/Repositorio de datos InfoVis - Gastos Mp.xlsx")

# Crea columnas vacías para las coordenadas
df["Latitud"] = None
df["Longitud"] = None

# Itera a través de las filas del DataFrame y geocodifica cada dirección
for index, row in df.iterrows():
    direccion = row["Ubicacion "]
    if pd.notna(direccion) and direccion.strip() != "":
        try:
            location = geolocator.geocode(direccion, timeout=10)
            if location:
                df.at[index, "Latitud"] = location.latitude
                df.at[index, "Longitud"] = location.longitude
        except Exception as e:
            print(f"Error al geocodificar '{direccion}': {str(e)}")

# Guarda el DataFrame con las coordenadas en un nuevo archivo Excel
df.to_excel("/Users/maria/Documents/ITBA MARIA/3 1Q/Visualizacion de la informacion/Repositorio de datos InfoVis - Gastos Mp_geocodedss.xlsx", index=False)

# Imprime el DataFrame con las columnas "Ubicacion", "Latitud" y "Longitud"
print(df[["Ubicacion ", "Latitud", "Longitud"]])


