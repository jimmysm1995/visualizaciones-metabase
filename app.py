import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboards", layout="wide")

# Crear las pestañas
tabs = st.tabs(["Etiquetas", "vinok", "Usuarios", "Grafana"])

# Contenido de la pestaña 1
with tabs[0]:
    st.header("Etiquetas")
    st.components.v1.iframe(
        "https://datalab.vinok.es/public/dashboard/9672fa9e-43b9-46ce-baa6-62ab6f1bd0f9",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 2
with tabs[1]:
    st.header("vinok")
    st.components.v1.iframe(
        "https://datalab.vinok.es/public/dashboard/61e8a95b-8a58-4c1d-9ce6-d788eeed96c3",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

# Contenido de la pestaña 3
with tabs[2]:
    st.header("Usuarios")
    st.components.v1.iframe(
        "https://datalab.vinok.es/public/dashboard/93d2f5b3-f721-47c7-b169-1ba06fe13e1c",  # Cambia el URL del segundo dashboard
        width=1200,
        height=800,
        scrolling=True,
    )

with tabs[3]:
    st.header("Grafana")
    grafana_url = "https://datalab.vinok.es/grafana/d-solo/deaz748cssagwd/vinok-dashboard?orgId=1&from=1737977136689&to=1737998736689&timezone=browser&panelId=9&__feature.dashboardSceneSolo"
    iframe_code = f"""
    <iframe src="{grafana_url}" width="1200" height="800" style="border: none; overflow: hidden;"></iframe>
    """
    st.markdown(iframe_code, unsafe_allow_html=True)

