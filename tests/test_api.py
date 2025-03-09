import pytest
import sys
import os
from fastapi.testclient import TestClient


from src.domain.repositories import NetworkTestResultRepository
from src.domain.entities import NetworkTestResult  # Correta
from src.application.services.network_test_service import NetworkTestService
from src.infrastructure.persistence.connection_factory import SessionLocal
from src.main import app 

client = TestClient(app)

def test_root():
    """Testa se a API está rodando corretamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de Monitoramento Ativa"}

def test_get_network_tests():
    """Testa o endpoint que retorna os testes de rede"""
    response = client.get("/network-tests")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # O retorno deve ser uma lista

def test_create_network_test():
    """Testa a criaçao de um novo teste de rede"""
    payload = {
        "site": "google.com",
        "latency": 20.5,
        "packet_loss": 0.0,
        "response_time": 0.45
    }
    response = client.post("/network-tests", json=payload)
    assert response.status_code == 201
    assert response.json()["site"] == "google.com"