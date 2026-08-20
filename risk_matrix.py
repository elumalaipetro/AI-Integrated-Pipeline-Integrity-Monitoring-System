import pandas as pd

df = pd.read_csv("pipeline_final_dataset.csv")

df["Risk_Index"] = (df["POF"] * df["CoF"]) / 100

def risk_category(x):
    if x >= 80:
        return "Critical"
    elif x >= 60:
        return "High"
    elif x >= 30:
        return "Medium"
    else:
        return "Low"

df["Risk_Matrix"] = df["Risk_Index"].apply(risk_category)

df.to_csv("pipeline_final_dataset.csv", index=False)

print("Risk Matrix Added Successfully")