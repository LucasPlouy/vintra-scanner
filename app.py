import streamlit as st
import requests

st.title("🧠 VINTRA Scanner (API)")

query = st.text_input("🔍 Recherche Vinted", "pull ralph homme")

if st.button("Scanner"):
    url = f"https://www.vinted.fr/api/v2/catalog/items"
    params = {
        "search_text": query,
        "per_page": 20,
        "page": 1
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        items = data.get("items", [])
        if not items:
            st.warning("Aucune annonce trouvée.")
        else:
            for item in items:
                titre = item["title"]
                prix = f"{item['price']} €"
                lien = f"https://www.vinted.fr{item['url']}"
                marque = item.get("brand_title", "Marque inconnue")
                score = "✅ À cop" if "ralph" in titre.lower() else "🟡 À voir"

                st.markdown(f"### [{titre}]({lien})")
                st.write(f"🏷️ Marque : {marque}")
                st.write(f"💰 Prix : {prix}")
                st.write(f"🧠 Score IA : {score}")
                st.write("---")
    except Exception as e:
        st.error(f"Erreur lors du scan : {e}")
