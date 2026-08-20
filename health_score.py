import pandas as pd

df = pd.read_csv("pipeline_dataset.csv")

def health_score(risk):
    if risk == "Low":
        return 90
    elif risk == "Medium":
        return 70
    else:
        return 40

df["Health_Score"] = df["Corrosion_Risk"].apply(health_score)

df.to_csv("pipeline_health_dataset.csv", index=False)

print("Health Score Added Successfully")