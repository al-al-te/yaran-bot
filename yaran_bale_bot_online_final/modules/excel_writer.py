
import pandas as pd
import os

def append_to_excel(data):
    file = "registered_users.xlsx"
    df = pd.DataFrame([data])
    if os.path.exists(file):
        df_existing = pd.read_excel(file)
        df = pd.concat([df_existing, df], ignore_index=True)
    df.to_excel(file, index=False)
