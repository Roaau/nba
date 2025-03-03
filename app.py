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

search_term = st.text_input("Ingresa el nombre de un jugador:")
if st.button("Buscar"):
    result = df[df["player_name"].str.contains(search_term, case=False)]
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
fig, ax = plt.subplots()
sns.histplot(df["age"], kde=True, ax=ax)
st.pyplot(fig)
st.write("Este histograma muestra la distribución de las edades de los jugadores.")

# Gráfica de barras: Puntos por equipo
st.subheader("Puntos por Partido por Equipo")
fig, ax = plt.subplots()
sns.barplot(x=df["team_abbreviation"], y=df["pts"], ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
st.write("Esta gráfica de barras muestra los puntos por partido promedio de cada equipo.")

# Gráfica scatter: Relación entre puntos y asistencias
st.subheader("Relación entre Puntos y Asistencias por Partido")
fig, ax = plt.subplots()
sns.scatterplot(x=df["pts"], y=df["ast"], hue=df["team_abbreviation"], ax=ax)
st.pyplot(fig)
st.write("Esta gráfica scatter muestra la relación entre los puntos y las asistencias por partido.")