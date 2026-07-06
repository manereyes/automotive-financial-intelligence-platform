## Script que funciona como un generador de unidades vehiculares

import pandas as pd
import random

### Lista con diccionarios de vehiculos

vehicle_catalog = [
{
        "brand": "Mercedes-Benz",
        "model": "CLA 200",
        "vehicle_type": "Sedan",
        "fuel_type": "Gasoline",
        "msrp": 720000
    },

    {
        "brand": "Mercedes-Benz",
        "model": "A 35",
        "vehicle_type": "Hatchback",
        "fuel_type": "Gasoline",
        "msrp": 1200000
    },

    {
        "brand": "Mercedes-Benz",
        "model": "GLC 300",
        "vehicle_type": "SUV",
        "fuel_type": "Gasoline",
        "msrp": 1100000
    },

    {
        "brand": "Mercedes-Benz",
        "model": "EQE 350",
        "vehicle_type": "EV",
        "fuel_type": "Electric",
        "msrp": 1450000
    },

    {
        "brand": "Mercedes-Benz",
        "model": "Clase G",
        "vehicle_type": "Luxury SUV",
        "fuel_type": "Gasoline",
        "msrp": 3500000
    }
]

# Definir los modelos existentes (años)
model_years = [2022, 2023, 2024, 2025]

# Lista de vehiculos vacía
vehicles = []

# Inicializar ID
vehicle_id = 1


# Ciclo que crea unidades de vehiculos
for vehicle in vehicle_catalog:
    for year in model_years:
        ## Simulación de depreciación - A mayor año, menor precio y mayor riesgo
        vehicle_age = 2025 - year
        depreciation_rate = 0.08
        
        # Esta linea calcula:
        # El valor actual del vehiculo = Precio de Venta Sugerido por el Fabricante (del vehiculo) * ((1 - tasa_de_depreciación)^edad_del_vehiculo)
        current_value = vehicle["msrp"] * ((1 - depreciation_rate) ** vehicle_age)
        
        # Simular riesgo dependiendo precio actual del vehiculo
        if current_value >= 2500000:
            risk_category = "High"
        elif current_value >= 1000000:
            risk_category = "Medium"
        else:
            risk_category = "Low"

        # Diccionario para crear el vehiculo
        vehicle_record = {
            "vehicle_id": vehicle_id,
            "brand": vehicle["brand"],
            "model": vehicle["model"],
            "vehicle_type": vehicle["vehicle_type"],
            "fuel_type": vehicle["fuel_type"],
            "model_year": year,
            "original_msrp": vehicle["msrp"],
            "current_value": current_value,
            "depreciation_rate": depreciation_rate,
            "risk_category": risk_category
        }

        vehicles.append(vehicle_record)
        
        vehicle_id += 1
        
vehicles_df = pd.DataFrame(vehicles)

# Exportar a csv
vehicles_df.to_csv("data/vehicles.csv", index=False)