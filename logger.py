
import pandas as pd
import os

LOG_FILE = "change_log.csv"

def log_change(emp_id, change_type, old_val, new_val):
    entry = pd.DataFrame([{
        "Emp ID": emp_id,
        "Change": change_type,
        "Old": old_val,
        "New": new_val
    }])
    if os.path.exists(LOG_FILE):
        entry.to_csv(LOG_FILE, mode='a', header=False, index=False)
    else:
        entry.to_csv(LOG_FILE, index=False)
