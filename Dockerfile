# Imagen base
FROM python:3.11-slim

WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer puerto
EXPOSE 8501

# Comando por defecto
CMD ["streamlit", "run", "web/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
