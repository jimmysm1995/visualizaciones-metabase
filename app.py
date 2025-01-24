import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboards", layout="wide")

# Crear las pestañas
tabs = st.tabs(["Dashboard 1", "Dashboard 2"])

# Contenido de la pestaña 1
with tabs[0]:
    st.header("Dashboard 2")
    st.components.v1.iframe(
        "https://9.223.32.5:3000/public/dashboard/9672fa9e-43b9-46ce-baa6-62ab6f1bd0f9",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 2
with tabs[1]:
    st.header("Dashboard 2")
    st.components.v1.iframe(
        "https://9.223.32.5:3000/public/dashboard/61e8a95b-8a58-4c1d-9ce6-d788eeed96c3",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

