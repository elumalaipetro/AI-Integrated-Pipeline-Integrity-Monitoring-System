import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "Pressure_bar": np.random.uniform(30, 100, n),
    "Temperature_C": np.random.uniform(25, 90, n),
    "Flow_Rate_m3_h": np.random.uniform(50, 500, n),
    "Pipe_Age_years": np.random.randint(1, 40, n),
    "Wall_Thickness_mm": np.random.uniform(5, 15, n),
    "Corrosion_Rate_mm_year": np.random.uniform(0.01, 0.30, n),
    "Soil_pH": np.random.uniform(4.5, 8.5, n),
    "Soil_Moisture_percent": np.random.uniform(10, 90, n),
}

df = pd.DataFrame(data)

# Corrosion risk score
risk_score = (
    0.30 * (df["Corrosion_Rate_mm_year"] / 0.30)
    + 0.20 * (df["Pipe_Age_years"] / 40)
    + 0.15 * (1 - df["Wall_Thickness_mm"] / 15)
    + 0.15 * (df["Soil_Moisture_percent"] / 90)
    + 0.10 * (df["Pressure_bar"] / 100)
    + 0.10 * (1 - df["Soil_pH"] / 8.5)
)

df["Corrosion_Risk"] = np.where(
    risk_score > 0.55, "High",
    np.where(risk_score > 0.35, "Medium", "Low")
)

# Simulated leak indicator
df["Leak_Indicator"] = np.where(
    (df["Pressure_bar"] > 80) &
    (df["Corrosion_Rate_mm_year"] > 0.20),
    1,
    0
)

# Save dataset
df.to_csv("pipeline_dataset.csv", index=False)

print("Dataset created successfully!")
print(f"Number of records: {len(df)}")
print(df.head())