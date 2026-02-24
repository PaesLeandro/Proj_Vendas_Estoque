# Configuração da imagem Python
# 1. Imagem base oficial do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Instala dependências do sistema necessárias para o PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Copia o ficheiro de requisitos e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o conteúdo do projeto para o container
COPY . .

# 6. Expõe a porta que o Flask utiliza
EXPOSE 5000

# 7. Comando para iniciar a aplicação
CMD ["python", "run.py"]