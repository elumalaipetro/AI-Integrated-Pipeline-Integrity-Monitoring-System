import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
prediction = ["High"]

if prediction[0] == "High":
    st.error(f"Predicted Corrosion Risk: {prediction[0]}")
elif prediction[0] == "Medium":
    st.warning(f"Predicted Corrosion Risk: {prediction[0]}")
else:
    st.success("Normal Monitoring")
    import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("corrosion_model.pkl")

st.title("AI-Based Pipeline Corrosion Risk Prediction")

pressure = st.number_input("Pressure (bar)", value=70.0)
temperature = st.number_input("Temperature (°C)", value=40.0)
flow_rate = st.number_input("Flow Rate (m3/h)", value=120.0)
pipe_age = st.number_input("Pipe Age (years)", value=8.0)
wall_thickness = st.number_input("Wall Thickness (mm)", value=12.0)
corrosion_rate = st.number_input("Corrosion Rate (mm/year)", value=0.5)
soil_ph = st.number_input("Soil pH", value=7.0)
soil_moisture = st.number_input("Soil Moisture (%)", value=30.0)

if st.button("Predict Risk"):
    data = pd.DataFrame({
        "Pressure_bar": [pressure],
        "Temperature_C": [temperature],
        "Flow_Rate_m3_h": [flow_rate],
        "Pipe_Age_years": [pipe_age],
        "Wall_Thickness_mm": [wall_thickness],
        "Corrosion_Rate_mm_year": [corrosion_rate],
        "Soil_pH": [soil_ph],
        "Soil_Moisture_percent": [soil_moisture]
    })

    prediction = model.predict(data)

if prediction[0] == "High":
    st.error(f"Predicted Corrosion Risk: {prediction[0]}")
elif prediction[0] == "Medium":
    st.warning(f"Predicted Corrosion Risk: {prediction[0]}")
else:
    st.success(f"Predicted Corrosion Risk: {prediction[0]}")

    import streamlit.components.v1 as components

with open("pipeline_risk_map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

st.subheader("Pipeline Risk Map")
components.html(map_html, height=600)
with open("pipeline_risk_map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

st.subheader("Pipeline Risk Map")
components.html(map_html, height=600)
import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("pipeline_final_dataset.csv")

# Title
st.title("AI Integrated Pipeline Monitoring Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Average RUL", round(df["RUL_Years"].mean(), 2))
col2.metric("Maximum RUL", round(df["RUL_Years"].max(), 2))
col3.metric("Minimum RUL", round(df["RUL_Years"].min(), 2))

# Dataset View
st.subheader("Pipeline Dataset")
st.dataframe(df)

# RUL Chart
st.subheader("Remaining Useful Life (RUL)")
st.bar_chart(df["RUL_Years"])

# Status Chart
st.subheader("Pipeline Status")
st.bar_chart(df["Status"].value_counts())
import matplotlib.pyplot as plt

st.subheader("Risk Matrix Distribution")

risk_counts = df["Risk_Matrix"].value_counts()

fig, ax = plt.subplots()
risk_counts.plot(kind="bar", ax=ax)
st.pyplot(fig)
st.subheader("Top 10 High Risk Pipelines")

top_risk = df.sort_values("Risk_Score", ascending=False).head(10)

st.dataframe(top_risk)
st.title("AI-Integrated Pipeline Integrity Monitoring System")
st.write("Corrosion Risk • Leak Detection • POF/COF • Risk Matrix • RUL")