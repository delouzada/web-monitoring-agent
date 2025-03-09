from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.persistence.connection_factory import SessionLocal
from src.application.services import NetworkTestService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/test-result")
def add_test_result(result_data: dict, db: Session = Depends(get_db)):
    service = NetworkTestService(db)
    return service.add_test_result(result_data)

@router.get("/api/results")
def get_all_results(db: Session = Depends(get_db)):
    service = NetworkTestService(db)
    return service.get_all_results()
