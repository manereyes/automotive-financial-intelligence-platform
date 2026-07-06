import pandas as pd
import numpy as np
import random
from faker import Faker

### ### ###

fake = Faker('es_MX')

NUM_CUSTOMERS = 10000
DATA_INCONSISTENCY = 0.02  # 2%

customers = []


# Ciclo que genera la información falsa
for customer_id in range(1, NUM_CUSTOMERS + 1):
    first_name = fake.first_name()
    last_name = fake.last_name()
    full_name = f"{first_name} {last_name}"
    age = random.randint(21, 70)
    #employment_years = random.randint(0, 35)
    
    # Generar y modelar segmento de cliente
    customer_segment = random.choices(
        ["Economic", "Standard", "Premium"],
        weights=[45, 40, 15],
        k=1
    )[0]
    
    if customer_segment == "Economic":
        monthly_income = random.randint(15000, 45000)
    elif customer_segment == "Standard":
        monthly_income = random.randint(45000, 120000)
    else:
        monthly_income = random.randint(120000, 350000)

    
    # Simular una generación de años de experiencia más realista
    career_start_age = random.randint(18, 25) # Calculamos la edad máxima de experiencia, asumiendo que cada cliente pudo haber entrado a trabajar desde los 18 a 25 años
    max_employment_years = max(age - career_start_age, 0) # Generamos el tope máximo de experiencia restando el inicio laboral menos la edad
    # Generar experiencia "coherente" dependiendo el segmento
    if customer_segment == "Premium":
        min_experience = max(int(max_employment_years * 0.5), 5)
        employment_years = random.randint(min(min_experience, max_employment_years), max_employment_years)
    elif customer_segment == "Standard":
        min_experience = max( int(max_employment_years * 0.3), 2)
        employment_years = random.randint(min(min_experience, max_employment_years), max_employment_years)
    else:
        employment_years = random.randint(0, max_employment_years)
    
    # Condicion que genera score crediticio relacionado con el ingreso
    if monthly_income >= 120000:
        credit_score = random.randint(720, 850)
    elif monthly_income >= 50000:
        credit_score = random.randint(650, 780)
    else:
        credit_score = random.randint(500, 680)
    
    # Simular deuda mensual del cliente
    monthly_debt = random.uniform(
        monthly_income * 0.1,
        monthly_income * 0.6
    )
    
    # Simulamos porcentaje de ingreso comprometido
    debt_to_income = round(monthly_debt / monthly_income, 2)
        
        
    # Modelar riesgo
    if credit_score >= 720 and debt_to_income < 0.30:
        risk_segment = "Low Risk"
    elif credit_score >= 650:
        risk_segment = "Medium Risk"
    else:
        risk_segment = "High Risk"
        
    
    # Simular errores en datos / inconsistencias
    if random.random() < DATA_INCONSISTENCY:
        monthly_income = -9999  # Valor erróneo para ingresos
        ## Agregar más inconsistencias a demás celdas ##
        
        
    # Crear el diccionario con la información del cliente
    customer = {
        "customer_id": customer_id,
        "full_name": full_name,
        "age": age,
        "monthly_income": monthly_income,
        "employment_years": employment_years,
        "credit_score": credit_score,
        "debt_to_income": debt_to_income,
        "region": fake.state(),
        "customer_segment": customer_segment,
        "risk_segment": risk_segment
    }
    
    # Añadir cliente a a lista
    customers.append(customer)
    
# Una vez finalizada la creación, crear DataFrame
customers_df = pd.DataFrame(customers)


# Exportar resultados
customers_df.to_csv("data/customers.csv", index=False)