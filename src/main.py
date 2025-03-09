from fastapi import FastAPI
from presentation.controllers.network_controller import router as network_router
from infrastructure.persistence.connection_factory import init_db
from infrastructure.scheduler.scheduler import start_scheduler
import threading

app = FastAPI(title="Web Monitoring Agent")

# Inicializa o banco
init_db()
app.include_router(network_router)

@app.on_event("startup")
async def startup_event():
    print("🟢 FastAPI inicializado, iniciando agendador em thread separada...")
    scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()
    print("🚀 Agendador iniciado!")