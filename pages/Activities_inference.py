import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils.components import header
from utils.plotly_charts import animated_activities_area



st.set_page_config(page_title="Mobility Patterns", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_csv("data/wp_act.csv")

df = cargar_datos()

def map_actividad(act):
    if act == "Casa":
        return "Home"
    elif act == "Trabajo":
        return "Work"
    else:
        return "Secondary"

df['timestamp'] = pd.to_datetime(df['timestamp'])


header()

st.markdown("<h1 style='text-align: left;'>ACTIVITIES INFERENCE</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left;font-size: 20px;'>This page shows the results of the activities inference model. Using raw GPS data, the model predicts the activity type. It could be used to understand mobility patterns in the city.</p>", unsafe_allow_html=True)


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
    st.metric(label="Average Home activities duration", value="7.42 h")
with col4:
    st.metric(label="Average Work activities duration", value="8.34 km")

df['actividad_cat'] = df['actividad'].apply(map_actividad)
df.set_index('timestamp', inplace=True)

resampled = (
    df.groupby('actividad_cat')
      .resample('10T')
      .agg({'ID': 'nunique'})
      .rename(columns={'ID': 'count'})
      .reset_index()
)

df_resampled = resampled.pivot(index='timestamp', columns='actividad_cat', values='count').fillna(0)

fig = animated_activities_area(df_resampled)
st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def load_html(filename):
  if "html_loaded" not in st.session_state:
    with st.spinner("Loading..."):
        with open(filename, "r", encoding="utf-8") as f:
            st.session_state.html_content = f.read()
            st.session_state.html_loaded = True
            return st.session_state.html_content

html_content=load_html("data/activities.html")




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
