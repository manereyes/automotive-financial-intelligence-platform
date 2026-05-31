import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

### Variables de entorno

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

### Connect Pooling

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"

## Engine para ejecución

engine = create_engine(DATABASE_URL)

## Conexión

try:
    connection = engine.connect()
    print(f"Connected to postgresql!")
    connection.close()

except Exception as e:
    print("Connection failed:")
    print(e)