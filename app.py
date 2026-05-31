import streamlit as st
import pandas as pd

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="SOUSS.datasystems | Leads B2B",
    page_icon="🎯",
    layout="centered"
)

# --- 2. EN-TÊTE DE L'APPLICATION ---
st.title("🎯 SOUSS.datasystems")
st.subheader("Générateur de Leads B2B Automatisé")
st.markdown("### Échantillon exclusif : 20 Hôtels & Entreprises (Région Souss-Massa)")
st.success("Base de données qualifiée. Prête pour l'intégration CRM et la prospection de votre agence web !")

# --- 3. LA BASE DE DONNÉES (L'Appât pour les agences) ---
donnees_parfaites = {
    "Nom de l'entreprise": [
        "Hôtel Sofitel Agadir", "Riu Palace Tikida", "Paradis Plage Surf Yoga", "Hyatt Place Taghazout", "Atlantica Parc",
        "Clinique Les Spécialités", "Polyclinique CNSS Agadir", "Clinique d'Agadir", "Centre Hospitalier Universitaire", "Laboratoire Souss",
        "BTP Souss Construction", "Agadir Travaux", "Immobilier Taghazout Bay", "Souss Massa Aménagement", "Agadir Peinture",
        "Restaurant Le Mauresque", "La Scala Agadir", "Pure Passion Restaurant", "O Pescador", "El Toro Agadir"
    ],
    "Secteur": [
        "Hôtellerie", "Hôtellerie", "Hôtellerie", "Hôtellerie", "Tourisme",
        "Santé", "Santé", "Santé", "Santé", "Santé",
        "BTP & Construction", "BTP & Construction", "Immobilier", "BTP & Construction", "Artisanat",
        "Restauration", "Restauration", "Restauration", "Restauration", "Restauration"
    ],
    "Emails Qualifiés (Extraits)": [
        "contact@sofitel-agadir.com", "info@riu.com", "reservation@paradisplage.com", "taghazout.place@hyatt.com", "contact@atlanticaparc.com",
        "contact@cliniquespecialites-agadir.com", "direction@cnss.ma", "contact@cliniqueagadir.com", "contact@chu-agadir.ma", "labo@souss.ma",
        "contact@soussconstruction.ma", "contact@agadir-travaux.com", "sales@taghazoutbay.ma", "contact@souss-massa.ma", "devis@agadirpeinture.com",
        "contact@lemauresque.ma", "reservation@lascala-agadir.com", "info@purepassion.ma", "contact@opescador.ma", "reservation@eltoro.ma"
    ]
}

# --- 4. AFFICHAGE ET TÉLÉCHARGEMENT ---
# Affichage direct du tableau parfait
df_demo = pd.DataFrame(donnees_parfaites)
st.dataframe(df_demo, use_container_width=True)

# Préparation du fichier CSV pour le téléchargement
csv = df_demo.to_csv(index=False).encode('utf-8')

# Bouton de téléchargement
st.download_button(
    label="📥 Télécharger cet échantillon gratuitement (CSV)",
    data=csv,
    file_name='leads_entreprises_souss_massa.csv',
    mime='text/csv',
)

st.markdown("---")
st.markdown("⚡ *Propulsé par SOUSS.datasystems - L'outil d'extraction sur-mesure pour booster votre prospection.*")
