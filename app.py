import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboards", layout="wide")

# Crear las pestañas
tabs = st.tabs(["Dashboard 1", "Dashboard 2"])

# Contenido de la pestaña 1
with tabs[0]:
    st.header("Dashboard 1")
    st.components.v1.iframe(
        "https://vinok-metabase.duckdns.org/public/dashboard/e46175a0-4cdf-4cf9-86fa-2b2772ee9285",
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 2
with tabs[1]:
    st.header("Dashboard 2")
    st.components.v1.iframe(
        "http://9vinok-metabase.duckdns.org/public/dashboard/61e8a95b-8a58-4c1d-9ce6-d788eeed96c3",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

