import Streamlit
print("etst")

import streamlit as st
import pandas as pd

# Interface Streamlit pour uploader plusieurs fichiers Excel
uploaded_files = st.file_uploader(
    "Téléchargez plusieurs fichiers Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    data_dict = {}  # Dictionnaire pour stocker les données
    row_index = 0  # Compteur d'index global

    for file in uploaded_files:
        # Charger chaque fichier Excel en DataFrame
        df = pd.read_excel(file, engine="openpyxl")

        # Convertir le DataFrame en dictionnaire (format liste de colonnes)
        df_dict = df.to_dict(orient="list")

        # Ajouter les données au dictionnaire principal avec un index unique
        for col, values in df_dict.items():
            if col in data_dict:
                data_dict[col].extend(values)  # Ajouter les nouvelles valeurs
            else:
                data_dict[col] = values  # Créer une nouvelle colonne

        # Mise à jour de l'index
        row_index += len(df)

    # Reconstruire un DataFrame final
    df_final = pd.DataFrame.from_dict(data_dict)

    st.write("Aperçu du DataFrame final :", df_final.head())

    # Télécharger le fichier final concaténé
    csv_data = df_final.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Télécharger le fichier CSV concaténé",
        data=csv_data,
        file_name="data_concatene.csv",
        mime="text/csv"
    )

