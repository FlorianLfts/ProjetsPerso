import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# Configuration de la page
st.set_page_config(page_title="Pagina web para la mejor del mundo", layout="wide")

# Ajout du logo
st.sidebar.image("logo.png", width=150)

# Sidebar avec menu latéral
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Cuanto te quiero :", ["Mucho", "Muchisimo", "Demasiado"])

submenu = st.sidebar.selectbox("Eres:", ["Guapa", "Increible", "Adorable"])

# Cases à cocher
st.sidebar.subheader("Filtros")
show_pro = st.sidebar.checkbox("Hacer cargar la barra")
show_chart2 = st.sidebar.checkbox("Para enamorarme cada día un poquito más", True)

# Liste d'idées de dates romantiques en espagnol
ideas_citas = [
    "Ir al acuario juntos",
    "Spa contigo",
    "Cena a la luz de las velas",
    "Paseo en la playa al atardecer",
    "Picnic en el parque",
    "Ver las estrellas juntos",
    "Viaje sorpresa de fin de semana",
    "Cocinar juntos una cena especial",
    "Maratón de películas románticas",
    "Visitar museos", "Besarte toda la noche en la cama", "Otros"
]

# Gestionnaire de dates
selected_date = st.date_input("Elige una fecha de cita: ")

# Sélecteur d'idée de date romantique
selected_cita = st.selectbox("Elige una idea para una cita romántica", ideas_citas)

# Affichage du titre principal
st.markdown("<h1 style='text-align: center;'>Pagina web para la mejor del mundo</h1>", unsafe_allow_html=True)

# Partie texte explicatif
st.write("Uno de los mejores regalos que fue en mi vida es haberte conocido, y queria crear esta pagina para celebrar lo increible que eres y mejorar tu dia")

query_params = st.experimental_get_query_params()

# Vérifier si des paramètres sont passés dans l'URL et afficher un message
if "name" in query_params:
    st.write(f"Bonjour, {query_params['name'][0]}!")
else:
    st.write("Bonjour, utilisateur inconnu!")

# Exemple pour récupérer un autre paramètre, comme l'âge
if "age" in query_params:
    st.write(f"Vous avez {query_params['age'][0]} ans.")
else:
    st.write("Votre âge est inconnu.")

# Barre de progression rouge remplie progressivement
progress_bar = st.empty()
progress = 0
for i in range(101):
    progress_bar.progress(i)
    sleep(0.02)  # Animation fluide
st.caption("Cuanto te echo de menos")

# Génération d'un nuage de points en forme de cœur
n = 300
np.random.seed(42)
t = np.linspace(0, 2 * np.pi, n)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Affichage des graphes en fonction des cases cochées
if show_chart2:
    st.subheader("Eso es completamente tuyo")
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='red', alpha=0.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    st.pyplot(fig)
