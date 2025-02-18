import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboards", layout="wide")

# Crear las pestañas
tabs = st.tabs(["Etiquetas", "vinok", "Usuarios", "Mapa Escaneo", "Usuario"])

# Contenido de la pestaña 1
with tabs[0]:
    st.header("Etiquetas")
    st.components.v1.iframe(
        "https://datalab.vinok.es/metabase/public/question/20-food-table?Foodcode=Pescados",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 2
with tabs[1]:
    st.header("vinok")
    st.components.v1.iframe(
        "https://datalab.vinok.es/metabase/public/dashboard/eb9796bc-cb79-4214-a0d1-0e23983d5aad?foodcode=Pescados",  # Cambia el URL del segundo dashboard
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
    st.header("Usuario")
    st.components.v1.iframe(
        "https://app.powerbi.com/reportEmbed?reportId=f3b8cf9d-3d61-4f96-990e-424a1cf11a44&autoAuth=true&ctid=0c1808cb-beab-4314-b799-5b2701c9eece", 
        width=1200, 
        height=800,
        scrolling=True
    )

