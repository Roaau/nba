import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Análisis de Jugadores de la NBA", page_icon="🏀")

# Título y autor
st.image("logo.jpeg", width=100)
st.title("Análisis de Jugadores de la NBA")
st.write("Autor: Jorge Roa - Matrícula: S22019943")

# Cargar dataset
@st.cache_data
def load_data():
    return pd.read_csv("all_seasons.csv")

df = load_data()

# Mostrar dataset con n filas
st.subheader("Visualización del Dataset")
n_filas = st.slider("Selecciona el número de filas a mostrar:", 5, 10000, 10)
st.write(df.head(n_filas))

# Búsqueda de jugadores
search_term = st.text_input("Ingresa el nombre de un jugador:")
if st.button("Buscar"):
    result = df[df["player_name"].str.contains(search_term, case=False)]
    if result.empty:
        st.warning("No se encontraron jugadores con ese nombre.")
    else:
        st.write(result)

# Filtrado de información
st.subheader("Filtrado de Jugadores")
columna_filtro = st.selectbox("Selecciona una columna para filtrar:", df.columns)
valores = df[columna_filtro].unique()
seleccion = st.multiselect(f"Filtrar por {columna_filtro}:", valores)
if seleccion:
    df_filtrado = df[df[columna_filtro].isin(seleccion)]
    st.write(df_filtrado)

# Histograma de edades
st.subheader("Distribución de Edades de los Jugadores")
bins = st.slider("Selecciona el número de intervalos (bins):", 5, 100, 20)
fig, ax = plt.subplots()
sns.histplot(df["age"], kde=True, bins=bins, ax=ax)
st.pyplot(fig)
st.write("Este histograma muestra la distribución de las edades de los jugadores.")

# Gráfica de barras: Puntos por equipo
st.subheader("Puntos por Partido por Equipo")
fig, ax = plt.subplots(figsize=(10, 8))
sns.barplot(x=df["pts"], y=df["team_abbreviation"], ax=ax, orient="h")
st.pyplot(fig)
st.write("Esta gráfica de barras muestra los puntos por partido promedio de cada equipo.")

# Gráfica scatter: Relación entre puntos y asistencias
st.subheader("Relación entre Puntos y Asistencias por Partido")
equipos_seleccionados = st.multiselect("Selecciona los equipos a visualizar:", df["team_abbreviation"].unique())
if equipos_seleccionados:
    df_filtrado = df[df["team_abbreviation"].isin(equipos_seleccionados)]
    fig, ax = plt.subplots()
    sns.scatterplot(x=df_filtrado["pts"], y=df_filtrado["ast"], hue=df_filtrado["team_abbreviation"], ax=ax)
    st.pyplot(fig)
else:
    st.warning("Por favor, selecciona al menos un equipo.")