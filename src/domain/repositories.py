from sqlalchemy.orm import Session
from domain.entities import NetworkTestResult
from infrastructure.persistence.connection_factory import SessionLocal

class NetworkTestResultRepository:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    def save(self, result: NetworkTestResult):
        """Salva um resultado de teste de rede no banco de dados."""
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return result

    def list_all(self):
        """Retorna todos os resultados armazenados no banco de dados."""
        return self.db.query(NetworkTestResult).all()