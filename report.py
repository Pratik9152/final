
import pandas as pd

def generate_csv_report(df, filename="gratuity_report.csv"):
    df.to_csv(filename, index=False)
    return filename
