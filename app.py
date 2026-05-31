import streamlit as st
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- 1. L'INTERFACE DE L'APPLICATION ---
st.set_page_config(page_title="SOUSS.datasystems", page_icon="🎯")
st.title("🎯 SOUSS.datasystems - Générateur de Leads B2B")
st.write("Extrayez automatiquement les contacts de vos futurs clients.")

# --- 2. LE MOTEUR (Le Sniper) ---
def sniper_emails(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        reponse = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(reponse.text, 'html.parser')
        texte_de_la_page = soup.get_text()
        
        pattern_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        emails_trouves = set(re.findall(pattern_email, texte_de_la_page))
        
        if emails_trouves:
            return ", ".join(emails_trouves)
        else:
            return "Aucun email trouvé"
            
    except Exception:
        return "Erreur de connexion"

# --- 3. L'ACTION ---
# Liste de prospection de démonstration
# --- 3. L'ACTION ---
# Liste des 20 agences cibles pour la prospection de Lundi
donnees_initiales = {
    "Nom de l'entreprise": [
        "Ajicod", "General Webers", "Web Assistances", "Media Dialna", "Fastboost Agency",
        "Technopek", "Viix Digital", "Mediaman", "Media Pulse", "Major Media",
        "Proweb", "Tweadup", "Ejahiz", "Coding Art", "Dev Maroc Web",
        "Web Linking", "Winu Maroc", "Développeur Informatique MA", "Aassou", "Energie Din"
    ],
    "Site Web": [
        "https://ajicod.com/fr",
        "https://generalwebers.com/",
        "https://www.webassistances.com/",
        "https://mediadialna.ma/",
        "https://fastboost.agency/",
        "https://technopek.ma/",
        "https://viixdigital.com/",
        "https://www.mediaman.ma/",
        "https://mediapulse.ma/contactez-nous/",
        "https://majormedia.marketing/",
        "https://www.proweb.ma/",
        "https://tweadup.com/",
        "https://caisse.ejahiz.ma/",
        "https://www.codingart.io/",
        "https://devmarocweb.com/",
        "https://www.weblinking.net/",
        "https://winumaroc.com/",
        "https://www.developpeur-informatique.ma/",
        "https://aassou.net/",
        "https://www.energiedin.com/?utm_source=mybusiness-agadir"
    ]
}
df_agences = pd.DataFrame(donnees_initiales)

# Le fameux bouton pour lancer la machine
if st.button("🚀 Lancer l'extraction des données"):
    
    # Éléments visuels pour faire patienter le client
    barre_progression = st.progress(0)
    statut_texte = st.empty()
    
    liste_butin = []
    total_lignes = len(df_agences)

    # La boucle d'automatisation
    for index, ligne in df_agences.iterrows():
        site_cible = ligne["Site Web"]
        nom_boite = ligne["Nom de l'entreprise"]
        
        statut_texte.text(f"🔄 Scan en cours : {nom_boite}...")
        
        resultat = sniper_emails(site_cible)
        liste_butin.append(resultat)
        
        # Mise à jour de la barre
        barre_progression.progress((index + 1) / total_lignes)
        time.sleep(1) # Petite pause pour faire travailler le logiciel visuellement

    df_agences["Emails Capturés"] = liste_butin
    
    # --- 4. LE RÉSULTAT VISUEL ---
    statut_texte.text("✅ Extraction terminée !")
    st.dataframe(df_agences, use_container_width=True)

    # Bouton de téléchargement
    csv = df_agences.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Télécharger les Leads (CSV)",
        data=csv,
        file_name='souss_datasystems_leads.csv',
        mime='text/csv',
    )
