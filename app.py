import streamlit as st
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Mapa de Transporte", layout="wide")

st.title("🚌 Visualización de Transporte Urbano")

# Crear mapa centrado en Lima
mapa = folium.Map(location=[-12.0464, -77.0428], zoom_start=13)

# Añadir puntos (ej. parada y punto de atracción)
folium.Marker(
    location=[-12.0464, -77.03],
    popup="Punto de Detracción",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mapa)

folium.Marker(
    location=[-12.05, -77.045],
    popup="Punto de Atracción",
    icon=folium.Icon(color="green", icon="star")
).add_to(mapa)

# Añadir línea (ruta)
folium.PolyLine(
    locations=[
        [-12.0464, -77.03],
        [-12.048, -77.035],
        [-12.05, -77.045]
    ],
    color="red",
    weight=4,
    tooltip="Línea 101 - Este a Oeste"
).add_to(mapa)

# Mostrar mapa en Streamlit
folium_static(mapa)
