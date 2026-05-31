## Script para cargar CSV de los vehiculos a Supabase ##

import pandas as pd

from src.config.database import supabase

vehicles_df = pd.read_csv("data/vehicles.csv")

vehicles_data = vehicles_df.to_dict(orient="records")

response = supabase.table("vehicles").insert(vehicles_data).execute()

print("Vehicles loaded successfully!")