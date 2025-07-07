import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🧠 VINTRA Scanner")

query = st.text_input("🔍 Recherche Vinted", "pull ralph homme")

if st.button("Scanner"):
    url = f"https://www.vinted.fr/vetements?search_text={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.select("div.feed-grid__item a")

    if not items:
        st.warning("Aucune annonce trouvée.")
    else:
        for a in items[:20]:
            try:
                titre = a.select_one(".catalogue-item__title").text.strip()
                prix = a.select_one(".catalogue-item__price").text.strip()
                lien = "https://www.vinted.fr" + a["href"]
                score = "✅ À cop" if "ralph" in titre.lower() else "🟡 À voir"

                st.markdown(f"### [{titre}]({lien})")
                st.write(f"💰 Prix : {prix}")
                st.write(f"🧠 Score IA : {score}")
                st.write("---")
            except:
                continue
