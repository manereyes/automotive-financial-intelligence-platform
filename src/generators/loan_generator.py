import pandas as pd
import numpy as np
import random
from datetime import timedelta
from pandas.tseries.offsets import BusinessDay


# Cargar Datasets

customers_df = pd.read_csv("data/customers.csv")
vehicles_df = pd.read_csv("data/vehicles.csv")

# Lista vacía de préstamos
loans = []

# Número de préstamos máximos a realizar
NUM_LOANS = 7000
# Fechas minimas y máximas para la generación de fechas de préstamos para análisis temporal y tendencias
START_DATE = pd.Timestamp("2020-01-01")
END_DATE = pd.Timestamp("2026-03-24")

# Ciclo que itera los préstamos
for loan_id in range(1, NUM_LOANS + 1):
    # Elegir cliente aleatorio para evaluarlo
    customer = customers_df.sample(1).iloc[0]
    # Elegir el vehiculo que quiere obtener (simulación realista por segmento del cliente y precio del vehiculo)
    if customer["customer_segment"] == "Premium":
        eligible_vehicles = vehicles_df[vehicles_df["current_value"] >= 1000000]
    elif customer["customer_segment"] == "Standard":
        eligible_vehicles = vehicles_df[(vehicles_df["current_value"] >= 500000) & (vehicles_df["current_value"] < 1000000)]
    else:
        eligible_vehicles = vehicles_df[vehicles_df["current_value"] < 500000]

    # Fallback de seguridad
    if eligible_vehicles.empty:
        eligible_vehicles = vehicles_df
<<<<<<< HEAD
=======
        
>>>>>>> e5d4729 (New Commit - Portfolio Overwiew Notebook created, EDA made)
        
    # Elegir un auto a financiar
    vehicle = eligible_vehicles.sample(1).iloc[0]
    

    #### Aquí simularemos el riesgo de crédito ####
    
    down_payment_percentage = random.uniform(0.10, 0.35)  # Generamos un enganche del 10% al 35% del precio del auto elegido
    down_payment = (vehicle["current_value"] * down_payment_percentage)  # Calculamos el valor a pagar de enganche multiplicando el valor por porcentaje de enganche
    loan_amount = (vehicle["current_value"] - down_payment)  # Calculamos el valor del préstamo restando el enganche al valor actual del auto
    term_months = random.choice([36, 48, 60, 72])  # Generamos una lista de meses a pagar y que se seleccione aleatoriamente
    
    # Simulamos la aprobación, donde un préstamos ya está autorizado al menos que encuentre una variable para ser rechazado
    approval_status = "Approved"
    
    
    # El préstamos se rechaza con base a la puntuación crediticia del cliente, DTI y salario mensual
    if customer["credit_score"] < 580:
        approval_status = "Rejected"
    elif customer["debt_to_income"] > 0.55:
        approval_status = "Rejected"
    elif (loan_amount > customer["monthly_income"] * 60):
        approval_status = "Rejected"
        
    
    # Aqui simularemos tasas de interés dinámicas que cambiarán dependiendo el segmento del cliente
    if customer["risk_segment"] == "Low Risk":
        interest_rate = random.uniform(7.5, 11.0)  # Un cliente del segmento de bajo riesgo puede amarrar una tasa de interés baja del 7.5% al 11% anual
    elif customer["risk_segment"] == "Medium Risk":
        interest_rate = random.uniform(11.0, 16.0) # Un cliente del segmento de medio riesgo puede amarrar una tasa de interés medio del 11% al 16% anual
    else:
        interest_rate = random.uniform(16.0, 24.0)  # Un cliente del segmento de alto riesgo puede amarrar una tasa de interés alta del 16% al 24% anual
        
    
    # Calcular mensualidad con intereses basada en la fórmula financiera de amortización
    monthly_interest_rate = (interest_rate / 100) / 12  # Convertimos el interés anual a interés mensual
    monthly_payment = (loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**term_months)) / ((1 + monthly_interest_rate)**term_months- 1)
    
    
    # Aqui simularemos y calcularemos la probabilidad de incumplimiento dependiendo el segmento del cliente
    
    if customer["risk_segment"] == "Low Risk":
        default_probability = random.uniform(0.01, 0.05)
    elif customer["risk_segment"] == "Medium Risk":
        default_probability = random.uniform(0.05, 0.15)
    else:
        default_probability = random.uniform(0.15, 0.35)
        
    
    # Simular fechas de creación de préstamo
    random_days = random.randint(0, (END_DATE - START_DATE).days)
    loan_start_date = (START_DATE + timedelta(days=random_days)).date()
    
    
    # Simular fechas de aprobación/rechazo de préstamo
    random_loan_waiting = random.randint(1, 5)
    approved_or_rejected_on = loan_start_date + BusinessDay(random_loan_waiting)  # Usamos BusinessDay para sumar días, sin contar fines de semanas
    
    
    
    # Resultado final - Diccionario
    loan = {
        "loan_id": loan_id,
        "customer_id": int(customer["customer_id"]),
        "vehicle_id": int(vehicle["vehicle_id"]),
        "loan_amount": round(loan_amount, 2),
        "down_payment": round(down_payment, 2),
        "interest_rate": round(interest_rate, 2),
        "term_months": term_months,
        "monthly_payment": round(monthly_payment, 2),
        "approval_status": approval_status,
        "default_probability": round(default_probability, 2),
        "loan_start_date": loan_start_date,
        "approved_or_rejected_on": approved_or_rejected_on
    }   
    
    # Meter a la lista de préstamos
    loans.append(loan)

loans_df = pd.DataFrame(loans)
loans_df.to_csv("data/loans.csv", index=False)