import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils.components import header
import json
from keplergl import KeplerGl



st.set_page_config(page_title="Mobility Patterns", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_csv("data/wp_trips.csv")

df = cargar_datos()
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by="timestamp")

header()

with open('data/config_wp.json', 'r') as f:
    loaded_config = json.load(f)
mapa = KeplerGl(height=400, data={'Mobility': df}, config=loaded_config)


html_string = mapa._repr_html_()
if isinstance(html_string, bytes):
    html_string = html_string.decode('utf-8')
else:
    html_string = html_string

html_fix = """
<script>
  setTimeout(() => {
    window.dispatchEvent(new Event('resize'));
  }, 200);
</script>
"""
html_inyectado = html_string + html_fix

components.html(html_inyectado, height=800, width=2000, scrolling=False)