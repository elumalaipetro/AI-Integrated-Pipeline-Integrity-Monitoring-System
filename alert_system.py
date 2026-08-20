import pandas as pd

df = pd.read_csv("pipeline_final_dataset.csv")

def alert_level(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 60:
        return "WARNING"
    else:
        return "NORMAL"

df["Alert"] = df["Risk_Score"].apply(alert_level)

df.to_csv("pipeline_alert_dataset.csv", index=False)

print("Alert System Added Successfully")
import pandas as pd

df = pd.read_csv("pipeline_final_dataset.csv")

def alert_level(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 60:
        return "WARNING"
    else:
        return "NORMAL"

df["Alert"] = df["Risk_Score"].apply(alert_level)

df.to_csv("pipeline_alert_dataset.csv", index=False)

print("Alert System Added Successfully")