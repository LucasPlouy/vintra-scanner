import streamlit as st
import requests

st.set_page_config(page_title="VINTRA Scanner", layout="wide")
st.title("🧠 VINTRA Scanner (v1)")

query = st.text_input("🔍 Recherche Vinted", "pull ralph homme")

if st.button("Scanner"):
    with st.spinner("Recherche en cours..."):
        try:
            res = requests.get(f"https://vintra-backend-api.lucasplouy.repl.co/api/search?q={query}")
            data = res.json()

            items = data.get("results", [])
            if not items:
                st.warning("Aucune annonce trouvée.")
            else:
                for item in items:
                    titre = item["title"]
                    lien = item["url"]
                    prix = item["price"]
                    marque = item["brand"]
                    score = item["score"]

                    st.markdown(f"### [{titre}]({lien})")
                    st.write(f"🏷️ Marque : {marque}")
                    st.write(f"💰 Prix : {prix}")
                    st.write(f"🧠 Score IA : {score}")
                    st.markdown("---")
        except Exception as e:
            st.error(f"Erreur lors de la recherche : {e}")
