import pandas as pd

df = pd.read_csv("pipeline_final_dataset.csv")

df["CoF"] = (df["Pressure_bar"] * df["Flow_Rate_m3_h"]) / 100

df.to_csv("pipeline_final_dataset.csv", index=False)

print("CoF Added Successfully")
print(df[["Pressure_bar","Flow_Rate_m3_h","CoF"]].head())