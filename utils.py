
import pandas as pd
from datetime import datetime

def process_file(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["Joining Date"] = pd.to_datetime(df["Joining Date"])
    df["Exit Date"] = pd.to_datetime(df["Exit Date"], errors="coerce")
    df["End Date"] = df["Exit Date"].fillna(pd.to_datetime("today"))
    df["Years Completed"] = ((df["End Date"] - df["Joining Date"]).dt.days / 365.25).round(2)
    df["Eligible"] = df["Years Completed"] >= 5
    df["Status"] = df["Exit Date"].apply(lambda x: "Exited" if pd.notna(x) else "Working")
    df["Gratuity Status"] = df.apply(lambda row: "✅ Eligible (Exited)" if row["Eligible"] and row["Status"]=="Exited"
                                     else ("✅ Eligible (Working)" if row["Eligible"] else "❌ Not Eligible"), axis=1)
    summary = f"Total Employees: {len(df)} | Eligible: {df['Eligible'].sum()}"
    return df, summary


def clear_data():
    import os
    if os.path.exists("employee_data.json"):
        os.remove("employee_data.json")

def save_processed_data(df):
    df.to_json("employee_data.json", orient="records", date_format="iso")
