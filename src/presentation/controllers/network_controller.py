from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.persistence.connection_factory import SessionLocal  # caso tenha movido config.py para persistence
from src.domain.repositories import NetworkTestResultRepository
from src.application.services.network_test_service import NetworkTestService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/run-tests", summary="Executa testes de rede (ping e HTTP)")
def run_network_tests(db: Session = Depends(get_db)):
    """
    Endpoint que executa os testes de rede e armazena os resultados no banco.
    """
    db = SessionLocal()
    repository = NetworkTestResultRepository(db)
    service = NetworkTestService(repository)
    
    """repository = NetworkTestResultRepository(db)
    service = NetworkTestService(repository)"""
    results = service.run_tests()
    return {"results": results}
