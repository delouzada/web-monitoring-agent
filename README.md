# Web Monitoring Agent

## 🚀 Sobre o Projeto

O **web-monitoring-agent** é uma aplicação FastAPI que realiza testes automáticos de monitoramento de rede para páginas web selecionadas:

- **Ping** (latência e perda de pacotes).
- **HTTP Test** (tempo de carregamento e códigos HTTP de retorno).

Os dados coletados são armazenados em um banco de dados PostgreSQL e disponibilizados através de dashboards intuitivos no Grafana.

---

### 🛠️ Requisitos do projeto

- Realizar testes periódicos nas URLs:
  - `google.com`
  - `youtube.com`
  - `rnp.br`

### 🗃️ Banco de dados:

- **PostgreSQL**

---

### 📁 Estrutura do projeto

```bash
web-monitoring-agent/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── src
    ├── main.py
    ├── application
    │   ├── dtos.py
    │   └── services
    │       └── network_test_service.py
    ├── domain
    │   ├── entities.py
    │   └── repositories.py
    ├── infrastructure
    │   ├── persistence
    │   │   ├── config.py
    │   │   └── init_db.py
    │   └── grafana
    │       └── provisioning
    │           ├── datasources.yaml
    │           ├── dashboards.yaml
    │           └── dashboards
    │               └── network_monitoring.json
    └── presentation
        └── network_controller.py
```

---

### 🚀 Stack Tecnológica
- **Backend:** Python (FastAPI)
- **Database:** PostgreSQL (SQLAlchemy)
- **Containers:** Docker & Docker-compose
- **Dashboards:** Grafana
- **CI/CD:** GitHub Actions

---

### 🚀 CI/CD

Pipeline automatizado usando GitHub Actions:

- Checkout do código
- Execução de testes (pytest)
- Build e push da imagem Docker para Docker Hub
- Deploy automático via SSH

---

### 🐳 Docker-compose

Containers utilizados:

- FastAPI (Aplicação principal)
- PostgreSQL
- Grafana

```yaml

version: "3.9"

services:
  postgres:
    image: postgres:latest
    container_name: postgres
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: monitoring
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./src/infrastructure/database/initial.sql:/docker-entrypoint-initdb.d/initial.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d monitoring"]
      interval: 10s
      timeout: 5s
      retries: 5

  monitoring-agent:
    build: .
    container_name: monitoring-agent
    environment:
      - PYTHONPATH=/app/src
      - DATABASE_URL=postgresql://admin:admin@postgres:5432/monitoring
    ports:
      - "8000:8000"
    depends_on:
      postgres:
        condition: service_healthy
   
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment: {}  # mapeamento vazio
    volumes:
      - grafana-data:/var/lib/grafana
      - ./src/infrastructure/grafana/provisioning/datasources.yaml:/etc/grafana/provisioning/datasources/datasources.yaml
      - ./src/infrastructure/grafana/provisioning/dashboards.yaml:/etc/grafana/provisioning/dashboards/dashboards.yaml
      - ./src/infrastructure/grafana/provisioning/dashboards/:/var/lib/grafana/dashboards/
    depends_on:
      monitoring-agent:
        condition: service_started
      postgres:
        condition: service_healthy
   

volumes:
  postgres-data:
  grafana-data:


```

---

### 📊 Grafana Dashboard

- Acesse o Grafana em `http://localhost:3000`.
- Configure o Data Source PostgreSQL utilizando as credenciais definidas.
- Dashboards pré-configurados para acompanhar latência, perdas de pacotes e tempos de resposta.

---

### 🔧 Execução Local

```bash
docker-compose up -d
```

---

### 📚 Documentação adicional
[📄 High-Level Design - HLD](assets/High-Level%20Design%20-%20HLD.pdf)

- Arquitetura do projeto (Hexagonal)
- Guia detalhado para deploy e integração contínua
- Orientações para utilização e personalização dos dashboards

---


