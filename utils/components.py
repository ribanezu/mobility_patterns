import streamlit as st
import os
import base64

def header():
    # Ruta del logo
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")

    # Inyectar CSS para estilo vertical centrado
    st.markdown("""
        <style>
        .header-vertical {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding-top: 0.5rem;
        }

        .header-logo {
            height: 40px;
            margin-bottom: 1rem;
        }

        .header-title {
            font-size: 2rem;
            font-weight: bold;
            text-transform: uppercase;
            margin: 0;
            color: var(--text-color);
            text-align: center;
        }

        .main > div:first-child {
            padding-top: 0rem;
        }

        [data-theme="light"] .header-title {
            color: #1f1f1f;
        }
        [data-theme="dark"] .header-title {
            color: #f5f5f5;
        }
        </style>
    """, unsafe_allow_html=True)

    # Renderizado del header vertical
    st.markdown(f"""
        <div class="header-vertical">
            <img src="data:image/png;base64,{_image_to_base64(logo_path)}" class="header-logo"/>
            <h1 class="header-title">Urban Mobility Patterns</h1>
        </div>
    """, unsafe_allow_html=True)

# Función auxiliar para convertir imagen a base64
def _image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

