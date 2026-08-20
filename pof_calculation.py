import pandas as pd

df = pd.read_csv("pipeline_final_dataset.csv")

df["POF"] = df["Risk_Score"]

df.to_csv("pipeline_final_dataset.csv", index=False)

print("POF Added Successfully")
print(df[["Risk_Score","POF"]].head())