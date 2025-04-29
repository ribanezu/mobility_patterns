import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils.components import header
from utils.plotly_charts import animated_unique_ids_area



st.set_page_config(page_title="Mobility Patterns", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_csv("data/wp_trips.csv")

df = cargar_datos()
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by="timestamp")

header()

st.markdown("<h1 style='text-align: left;'>DEMAND PROFILE</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left;font-size: 20px;'>This page shows data collected in the last day. The data collected with Indra's MaaS app over the last day is shown. The data has been properly anonymized</p>", unsafe_allow_html=True)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

last_update = df["timestamp"].max().strftime("%Y-%m-%d")
unique_devices = df["ID"].nunique() 

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Last Update", value=last_update)
with col2:
    st.metric(label="Unique Devices", value=unique_devices)
with col3:
    st.metric(label="Number of Trips", value="432")
with col4:
    st.metric(label="Average Trip Length", value="8.45 km")

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)
df_resampled = df.resample('10T').apply(lambda x: x['ID'].nunique())


fig = animated_unique_ids_area(df_resampled)
st.plotly_chart(fig, use_container_width=True)

@st.cache_resource
def load_html(filename):
  if "html_loaded" not in st.session_state:
    with st.spinner("Loading..."):
        with open(filename, "r", encoding="utf-8") as f:
            st.session_state.html_content = f.read()
            st.session_state.html_loaded = True
            return st.session_state.html_content

html_content=load_html("data/waypoints.html")




html_fix = """
<script>
  setTimeout(() => {
    window.dispatchEvent(new Event('resize'));
  }, 200);
</script>
"""
html_inyectado = html_content + html_fix

components.html(html_inyectado, height=800, width=2000, scrolling=False)

st.markdown("<p style='text-align: center;'>Below you can analyze the raw data.</p>", unsafe_allow_html=True)

with st.expander("Show data..."):
    st.dataframe(df)
