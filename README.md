# Web Monitoring Agent

## ?? Sobre o Projeto

O **web-monitoring-agent** � uma aplica��o FastAPI que realiza testes autom�ticos de monitoramento de rede para p�ginas web selecionadas:

- **Ping** (lat�ncia e perda de pacotes).
- **HTTP Test** (tempo de carregamento e c�digos HTTP de retorno).

Os dados coletados s�o armazenados em um banco de dados PostgreSQL e disponibilizados atrav�s de dashboards intuitivos no Grafana.

---

### ??? Requisitos do projeto

- Realizar testes peri�dicos nas URLs:
  - `google.com`
  - `youtube.com`
  - `rnp.br`

### ??? Banco de dados:

- **PostgreSQL**

---

### ?? Estrutura do projeto

```bash
web-monitoring-agent/
??? docker-compose.yml
??? Dockerfile
??? requirements.txt
??? src
    ??? main.py
    ??? application
    ?   ??? dtos.py
    ?   ??? services
    ?       ??? network_test_service.py
    ??? domain
    ?   ??? entities.py
    ?   ??? repositories.py
    ??? infrastructure
    ?   ??? persistence
    ?   ?   ??? config.py
    ?   ?   ??? init_db.py
    ?   ??? grafana
    ?       ??? provisioning
    ?           ??? datasources.yaml
    ?           ??? dashboards.yaml
    ?           ??? dashboards
    ?               ??? network_monitoring.json
    ??? presentation
        ??? network_controller.py
```

---

### ?? Stack Tecnol�gica
- **Backend:** Python (FastAPI)
- **Database:** PostgreSQL (SQLAlchemy)
- **Containers:** Docker & Docker-compose
- **Dashboards:** Grafana
- **CI/CD:** GitHub Actions

---

### ?? CI/CD

Pipeline automatizado usando GitHub Actions:

- Checkout do c�digo
- Execu��o de testes (pytest)
- Build e push da imagem Docker para Docker Hub
- Deploy autom�tico via SSH

---

### ?? Docker-compose

Containers utilizados:

- FastAPI (Aplica��o principal)
- PostgreSQL
- Grafana

```yaml
version: "3.9"
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: monitoring
    ports:
      - "5432:5432"

  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:password@postgres/monitoring
    depends_on:
      - postgres

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana

volumes:
  grafana-data:
```

---

### ?? Grafana Dashboard

- Acesse o Grafana em `http://localhost:3000`.
- Configure o Data Source PostgreSQL utilizando as credenciais definidas.
- Dashboards pr�-configurados para acompanhar lat�ncia, perdas de pacotes e tempos de resposta.

---

### ?? Execu��o Local

```bash
docker-compose up -d
```

---

### ?? Documenta��o adicional

- Arquitetura do projeto (Hexagonal)
- Guia detalhado para deploy e integra��o cont�nua
- Orienta��es para utiliza��o e personaliza��o dos dashboards

---



