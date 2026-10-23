import joblib
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
model = joblib.load(ROOT / "notebooks" / "models" / "sdg7_electricity_access_model.pkl")
data = pd.read_csv(ROOT / "data" / "processed" / "sdg7_clean.csv")

FEATURES = ["gdp_per_capita_log", "urban_pop_pct", "energy_per_capita", "carbon_intensity_elec",
            "fossil_share_elec", "hydro_share_elec", "solar_share_elec", "wind_share_elec", "population"]

st.set_page_config(page_title="SDG 7 Electricity Access Predictor")
st.title("SDG 7: Predicting electricity access")
st.caption("Move the sliders to see the model's predicted share of a country's population with electricity.")

gdp = st.slider("GDP per capita (US$)", 200, 100000, 3000, step=100)
urban = st.slider("Urban population (%)", 10, 100, 55)
fossil = st.slider("Fossil share of electricity (%)", 0, 100, 70)
hydro = st.slider("Hydro share of electricity (%)", 0, 100, 10)

inputs = data[FEATURES].median()          # other inputs held at typical values
inputs["gdp_per_capita_log"] = np.log(gdp)
inputs["urban_pop_pct"] = urban
inputs["fossil_share_elec"] = fossil
inputs["hydro_share_elec"] = hydro

pred = float(np.clip(model.predict(inputs.to_frame().T)[0], 0, 100))
st.metric("Predicted electricity access", f"{pred:.1f}%")
st.caption("Typical error is about 19 percentage points. The model describes patterns, not causes.")