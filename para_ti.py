
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

# Ajout du logo
st.image("logo.png", width=150)

# Sidebar avec menu latéral
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Cuanto te quiero :", ["Mucho", "Muchisimo", "Demasiado"])
submenu = st.sidebar.selectbox("Sous-menu", ["Vue 1", "Vue 2", "Vue 3"])

# Cases à cocher
st.sidebar.subheader("Filtres")
show_pro = st.sidebar.checkbox("Afficher uniquement Pro = 'A'")
show_chart1 = st.sidebar.checkbox("Afficher Graphique 1", True)
show_chart2 = st.sidebar.checkbox("Afficher Graphique 2", True)
show_chart3 = st.sidebar.checkbox("Afficher Graphique 3", True)

# Liste de citations romantiques en espagnol
citas_romanticas = [
    "Ir al acuario juntos",
    "Spa contigo",
    "Cena a la luz de las velas",
    "Paseo en la playa al atardecer",
    "Picnic en el parque",
    "Ver las estrellas juntos",
    "Viaje sorpresa de fin de semana",
    "Cocinar juntos una cena especial",
    "Maratón de películas románticas",
    "Visitar museos"
]


# Gestionnaire de dates
selected_date = st.date_input("Sélectionner une date")

# Sélecteur d'idée de date romantique
selected_cita = st.selectbox("Elige una idea para una cita romántica", ideas_citas)

# Affichage du titre principal
st.markdown("<h1 style='text-align: center;'>Tableau de Bord Streamlit</h1>", unsafe_allow_html=True)

# Partie texte explicatif
st.write("Ce tableau de bord interactif permet d'explorer les données et d'afficher différents graphiques en fonction des filtres sélectionnés.")

# Barre horizontale avec légende
st.progress(100)
st.caption("Cuanto te echo de menos")

# Génération d'un nuage de points en forme de cœur
n = 300
np.random.seed(42)
t = np.linspace(0, 2 * np.pi, n)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Affichage des graphes en fonction des cases cochées
if show_chart2:
    st.subheader("Graphique 2 - Nuage de points en forme de cœur")
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='red', alpha=0.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    st.pyplot(fig)

if show_chart3:
    st.subheader("Graphique 3 - Boîte à moustaches")
    fig, ax = plt.subplots()
    data = pd.DataFrame({
        "Valeur1": np.random.randn(100) * 10 + 50,
        "Valeur2": np.random.randn(100) * 5 + 20
    })
    data.boxplot(column=["Valeur1", "Valeur2"], ax=ax)
    st.pyplot(fig)
