import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin@postgres:5432/monitoring")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db(max_retries: int = 10, delay: int = 3):
    retries = 0
    while retries < max_retries:
        try:
            Base.metadata.create_all(bind=engine)
            print("Banco de dados inicializado com sucesso.")
            return
        except OperationalError as e:
            retries += 1
            print(f"Erro ao conectar no banco, tentativa {retries}/{max_retries}. Aguardando {delay} segundos...")
            time.sleep(delay)
    raise Exception("Não foi possível conectar ao PostgreSQL após várias tentativas.")