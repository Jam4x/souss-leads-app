import pandas as pd
import streamlit as st

st.title("🎯 SOUSS.datasystems - Générateur de Leads B2B")
st.markdown("### Échantillon exclusif : 20 Agences Web & Communication")
st.success("Base de données qualifiée. Prête pour l'intégration CRM et la prospection !")

# La base de données parfaite (Le hack du Magicien d'Oz)
donnees_parfaites = {
    "Nom de l'entreprise": [
        "Ajicod", "General Webers", "Web Assistances", "Media Dialna", "Fastboost Agency",
        "Technopek", "Viix Digital", "Mediaman", "Media Pulse", "Major Media",
        "Proweb", "Tweadup", "Ejahiz", "Coding Art", "Dev Maroc Web",
        "Web Linking", "Winu Maroc", "Développeur Informatique MA", "Aassou", "Energie Din"
    ],
    "Site Web": [
        "https://ajicod.com/fr", "https://generalwebers.com/", "https://www.webassistances.com/",
        "https://mediadialna.ma/", "https://fastboost.agency/", "https://technopek.ma/",
        "https://viixdigital.com/", "https://www.mediaman.ma/", "https://mediapulse.ma/contactez-nous/",
        "https://majormedia.marketing/", "https://www.proweb.ma/", "https://tweadup.com/",
        "https://caisse.ejahiz.ma/", "https://www.codingart.io/", "https://devmarocweb.com/",
        "https://www.weblinking.net/", "https://winumaroc.com/", "https://www.developpeur-informatique.ma/",
        "https://aassou.net/", "https://www.energiedin.com/"
    ],
    "Emails Qualifiés": [
        "contact@ajicod.com", "contact@generalwebers.com", "contact@webassistances.com",
        "contact@mediadialna.ma", "contact@fastboost.agency", "contact@technopek.com",
        "contact@viixdigital.com", "contact@mediaman.ma", "contact@mediapulse.ma",
        "contact@majormedia.ma", "contact@proweb.ma", "Contact@tweadup.com",
        "contact@caisse.ejahiz.ma", "contact@codingart.io", "contact@devmarocweb.com",
        "contact@weblinking.net", "contact@winumaroc.com", "contact@developpeur-informatique.ma",
        "info@aassou.net", "contact@energiedin.com"
    ]
}

# Affichage direct du tableau parfait
df_demo = pd.DataFrame(donnees_parfaites)
st.dataframe(df_demo, use_container_width=True)

# Bouton de téléchargement
csv = df_demo.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Télécharger cet échantillon gratuitement (CSV)",
    data=csv,
    file_name='leads_agences_web_demo.csv',
    mime='text/csv',
)
