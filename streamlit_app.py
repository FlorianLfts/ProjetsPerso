import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

# Ajouter un logo centré dans la page principale (en haut de l'application)
st.image("logo.png", width=150)

# Menu latéral avec streamlit-option-menu
with st.sidebar:
    # Menu avec des options stylisées
    selected = option_menu(
        menu_title="Option-Menu",  # Nom du menu
        options=["Accueil", "Analyse", "Rapports"],  # Options
        icons=["house", "bar-chart", "file-earmark-text"],  # Icônes pour chaque option
        menu_icon="cast",  # Icône du menu principal
        default_index=0,  # L'option par défaut
        styles={
            "container": {"background-color": "#f0f0f5", "padding": "5px"},  # Conteneur
            "icon": {"color": "#3B5998", "font-size": "18px"},  # Icônes
            "nav-link": {"font-size": "16px", "text-align": "center", "padding": "10px", "color": "#000000"},
            "nav-link-selected": {"background-color": "#3B5998", "color": "white"},  # Sélectionner une option
        }
    )

# Cases à cocher dans la barre latérale
st.sidebar.subheader("Filtres")
show_pro = st.sidebar.checkbox("Afficher uniquement Pro = 'A'")
show_chart1 = st.sidebar.checkbox("Afficher Graphique 1", True)
show_chart2 = st.sidebar.checkbox("Afficher Graphique 2", True)
show_chart3 = st.sidebar.checkbox("Afficher Graphique 3", True)

# Génération d'un dataframe fictif
np.random.seed(42)
data = pd.DataFrame({
    "Pro": np.random.choice(["A", "B", "C"], size=100),
    "Valeur1": np.random.randn(100) * 10 + 50,
    "Valeur2": np.random.randn(100) * 5 + 20
})

# Filtrer les données si la case est cochée
if show_pro:
    data = data[data["Pro"] == "A"]

# Affichage du titre principal
st.markdown("<h1 style='text-align: center;'>Tableau de Bord Streamlit</h1>", unsafe_allow_html=True)

# Partie texte explicatif
st.write("Ce tableau de bord interactif permet d'explorer les données et d'afficher différents graphiques en fonction des filtres sélectionnés.")

# Affichage des graphes en fonction des cases cochées
col1, col2 = st.columns(2)

if show_chart1:
    with col1:
        st.subheader("Graphique 1 - Histogramme")
        fig, ax = plt.subplots()
        data["Valeur1"].hist(bins=20, ax=ax, color='blue', alpha=0.7)
        st.pyplot(fig)

if show_chart2:
    with col2:
        st.subheader("Graphique 2 - Nuage de points")
        fig, ax = plt.subplots()
        ax.scatter(data["Valeur1"], data["Valeur2"], color='red', alpha=0.6)
        ax.set_xlabel("Valeur1")
        ax.set_ylabel("Valeur2")
        st.pyplot(fig)

if show_chart3:
    st.subheader("Graphique 3 - Boîte à moustaches")
    fig, ax = plt.subplots()
    data.boxplot(column=["Valeur1", "Valeur2"], ax=ax)
    st.pyplot(fig)

