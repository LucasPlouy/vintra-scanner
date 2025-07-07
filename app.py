import streamlit as st
import requests

st.title("🧠 VINTRA Scanner (API Full)")

query = st.text_input("🔍 Recherche Vinted", "ralph lauren")

if st.button("Scanner"):
    url = "https://www.vinted.fr/api/v2/catalog/items"
    params = {
        "search_text": query,
        "catalog_ids": "1904",  # vêtements hommes
        "per_page": 20,
        "page": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        items = data.get("items", [])
        if not items:
            st.warning("Aucune annonce trouvée.")
        else:
            for item in items:
                titre = item.get("title", "Titre inconnu")
                prix = f"{item.get('price', 0)} €"
                url_item = f"https://www.vinted.fr{item.get('url')}"
                marque = item.get("brand_title", "Marque inconnue")
                score = "✅ À cop" if "ralph" in titre.lower() else "🟡 À voir"

                st.markdown(f"### [{titre}]({u)

