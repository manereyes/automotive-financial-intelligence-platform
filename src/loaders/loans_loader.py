## Script para cargar CSV de los préstamos a Supabase ##

import pandas as pd
import numpy as np

from src.config.database import supabase

loans_df = pd.read_csv("data/loans.csv")

loans_df = loans_df.replace({np.nan: None})

loans_data = loans_df.to_dict(orient="records")

response = supabase.table("loans").insert(loans_data).execute()

print("Loans loaded successfully!")