from apscheduler.schedulers.background import BackgroundScheduler
from application.services.network_test_service import NetworkTestService
from domain.repositories import NetworkTestResultRepository
from infrastructure.persistence.connection_factory import SessionLocal
from infrastructure.config.config_loader import config  # Importa a configuração
import time

INTERVAL = config["monitoring"]["interval_seconds"]  # Tempo de agendamento

def scheduled_job():
    """Função que será executada periodicamente para rodar os testes de rede."""
    print(f"🔄 Executando job agendado... (intervalo: {INTERVAL}s)")

    db = SessionLocal()
    try:
        repository = NetworkTestResultRepository(db)
        service = NetworkTestService(repository)
        results = service.run_tests()
        print(f"✅ Job executado com sucesso: {results}")
    except Exception as e:
        print(f"❌ Erro no job agendado: {e}")
    finally:
        db.close()

def start_scheduler():
    print(f"🚀 Iniciando o agendador APScheduler com intervalo de {INTERVAL} segundos...")

    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', seconds=INTERVAL)
    scheduler.start()

    # Mantém o agendador rodando no Docker
    while True:
        print("⏳ Agendador está rodando...")
        time.sleep(60)
