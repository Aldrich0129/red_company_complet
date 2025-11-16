import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Red Dinámica", layout="wide")

st.title("Visualización Interactiva de Redes – Versión Segura")

st.sidebar.header("Seleccione una visualización")

options = {
    "Red Global (Años)": "global_dynamic_years.html",
    "Red de Riesgo (Años)": "risk_dynamic_years.html",
    "Red de Rentabilidad (Años)": "return_dynamic_years.html",
    "Red Global por Variables": "global_dynamic_variables.html"
}

choice = st.sidebar.selectbox("Visualización", list(options.keys()))
html_file = options[choice]

st.sidebar.write("---")
st.sidebar.write("© Tu Nombre / Red de Empresas Mineras")

# 读取本地 HTML 并嵌入
with open(html_file, "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=800, scrolling=True)
