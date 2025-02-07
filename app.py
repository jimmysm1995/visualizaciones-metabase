import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboards", layout="wide")

# Crear las pestañas
tabs = st.tabs(["Etiquetas", "vinok", "Usuarios", "Mapa Escaneo", "Bodegas"])

# Contenido de la pestaña 1
with tabs[0]:
    st.header("Etiquetas")
    st.components.v1.iframe(
        "https://datalab.vinok.es/metabase/public/dashboard/9672fa9e-43b9-46ce-baa6-62ab6f1bd0f9",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 2
with tabs[1]:
    st.header("vinok")
    st.components.v1.iframe(
        "https://datalab.vinok.es/metabase/public/dashboard/eb9796bc-cb79-4214-a0d1-0e23983d5aad",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 3
with tabs[2]:
    st.header("Usuarios")
    st.components.v1.iframe(
        "https://datalab.vinok.es/metabase/public/dashboard/93d2f5b3-f721-47c7-b169-1ba06fe13e1c",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña Grafana
with tabs[3]:
    st.header("Mapa")
    st.components.v1.iframe(
        "https://datalab.vinok.es/grafana/d-solo/deaz748cssagwd/vinok-dashboard?orgId=1&panelId=10&var-productName=Finca_Valdelayegua", 
        width=1200, 
        height=800,
        scrolling=True
    )

# Contenido de la pestaña Grafana
with tabs[4]:
    st.header("Bodegas")
    st.components.v1.iframe(
        "https://datalab.vinok.es/grafana/d-solo/deaz748cssagwd/vinok-dashboard?orgId=1&panelId=7&var-companyName=Bodega+Matarromera", 
        width=1200, 
        height=800,
        scrolling=True
    )
