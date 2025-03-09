FROM python:3.11-slim

WORKDIR /app

# Copia todos os arquivos da aplicação
COPY . .

# Copia especificamente o script para garantir que ele esteja no lugar certo
COPY src/infrastructure/config/wait-for-it.sh /app/src/infrastructure/config/wait-for-it.sh

# Dá permissão de execução ao script
RUN chmod +x /app/src/infrastructure/config/wait-for-it.sh



# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala o pacote iputils-ping
RUN apt-get update && apt-get install -y iputils-ping

# Copia o código fonte
COPY ./src ./src

# Inicia a aplicação FastAPI com Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]