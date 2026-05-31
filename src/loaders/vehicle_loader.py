## Script para cargar CSV de los vehiculos a Supabase ##

import pandas as pd

from src.config.database import engine

vehicles_df = pd.read_csv(
    "data/vehicles.csv"
)

vehicles_df.to_sql(
    "vehicles",
    engine,
    if_exists="append",
    index=False
)