import streamlit as st
import pandas as pd

st.set_page_config(page_title="FilmGPT", layout="wide")

st.title("🎥 ShiftPoint: Query Game Moments")

st.write("Ask about momentum shifts, scoring droughts, or player performance across any tagged game.")

# Load your dataset
df = pd.read_csv("film_data.csv")

# Simple search
query = st.text_input("Search scenario, player, or quarter (e.g. 'Q2', 'transition')")

if query:
    results = df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    st.subheader("Results:")
    st.dataframe(results)
    if not results.empty:
        for link in results["YouTube Link"]:
            st.markdown(f"[📺 Watch Clip]({link})")
