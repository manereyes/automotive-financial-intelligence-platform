## Script para cargar CSV de los clientes a Supabase ##

import pandas as pd

from platform.config.database import supabase

customers_df = pd.read_csv("data/customers.csv")

customers_data = customers_df.to_dict(orient="records")

response = supabase.table("customers").insert(customers_data).execute()

print("Customers loaded successfully!")